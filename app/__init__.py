#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __init__.py

import os, sys, json, pathlib
from bson.objectid import ObjectId
from flask import (
    Flask,
    request,
    render_template,
    url_for,
    Response,
    session,
    redirect,
    flash,
)
from flask_socketio import SocketIO, emit
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from datetime import date

clients = []

app = Flask(__name__, instance_relative_config=True)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
socketio = SocketIO(app)


@app.route("/")
def index():
    # check session.
    if "email" in session:
        email = session["email"]
        return redirect(url_for("events"))

    return render_template("login.html")


@app.route("/login_validation", methods=["POST"])
def login_validation():
    user = mongo.db.user
    login_user = user.find_one({"email": request.form["email"]})

    if login_user:
        if bcrypt.check_password_hash(login_user["pass"], request.form["pass"]):
            session["email"] = request.form["email"]
            return redirect(url_for("events"))
        else:
            flash(message="Email e/ou Senha são inválidos!", category="danger")
            return redirect(url_for("login"))
    else:
        flash(message="Email não cadastrado!", category="danger")
        return redirect(url_for("login"))


@app.route("/login")
def login():
    if "email" in session:
        email = session["email"]
        return redirect(url_for("events"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user = mongo.db.user
        existing_user = user.find_one({"email": request.form["email"]})

        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(request.form["pass"]).decode(
                "utf-8"
            )

            user.insert(
                {
                    "name": request.form["name"],
                    "email": request.form["email"],
                    "pass": hashpass,
                }
            )

            session["email"] = request.form["email"]

            return redirect(url_for("events"))

        flash(message="Esse email já foi cadastrado!", category="danger")
        return render_template("register.html")

    return render_template("register.html")


@app.route("/readers", methods=["GET", "POST"])
def readers():
    if "email" in session:
        id_event = request.args["id"]
        email = session["email"]
        data = mongo.db.reader
        return (
            render_template("readers.html", readers=data.find(), readers2=data.find()),
            200,
        )

    return redirect(url_for("login"))


@app.route("/register_reader", methods=["POST", "GET"])
def register_reader():
    if "email" in session:
        if request.method == "POST":
            reader = mongo.db.reader
            reader.insert(
                {
                    "name": request.form["name"],
                    "ip": request.form["ip"],
                    "port": request.form["port"],
                    "status": "1",
                }
            )
            flash(message="Reader Adicionado!", category="success")
            return redirect(url_for("readers"))
    return redirect(url_for("login"))


@app.route("/update_reader")
def update_reader():
    if "email" in session:
        if request.method == "POST":
            reader = mongo.db.reader
            reader.update(
                {"name": request.form["name"], "ip": request.form["ip"], "status": "1"}
            )
        flash(message="Reader Adicionado!", category="success")
        return redirect(url_for("readers"))


@app.route("/delete_reader")
def delete_reader():
    if "email" in session:
        email = session["email"]
        return render_template("readers.html"), 200

    return redirect(url_for("readers"))


@app.route("/events")
def events():
    if "email" in session:
        email = session["email"]
        data = mongo.db.event
        events = data.find()
        return render_template("events.html", events=events), 200

    return redirect(url_for("login"))


@app.route("/register_event", methods=["POST", "GET"])
def register_event():
    if request.method == "POST":
        event = mongo.db.event
        event.insert(
            {
                "name": request.form["name"],
                "date": request.form["date"],
                "organization": request.form["organization"],
                "city": request.form["city"],
                "status": "0",
            }
        )
        flash(message="Evento Salvo!", category="success")

        return redirect(url_for("events"))


@app.route("/delete_event", methods=["POST", "GET"])
def delete_event():
    if "email" in session:
        if request.method == "GET":
            id_event = request.args["id"]
            mongo.db.event.delete_one({"_id": ObjectId(id_event)})
            flash(message="Evento Excluido!", category="success")

            return redirect(url_for("events"))

    return redirect(url_for("login"))


@app.route("/download_report", methods=["POST", "GET"])
def download_report():
    if "email" in session:
        if request.method == "GET":
            data = mongo.db.tag
            tags = data.find()

            today = date.today()
            d = today.strftime("%d-%m-%Y")

            file_name = "report-"+d

            generator = (cell for tag in tags for cell in str(tag) + "\n")

            return Response(
                generator,
                mimetype="text/json",
                headers={
                    "Content-Disposition": "attachment; filename=" + file_name + ".json"
                },
            )

    return redirect(url_for("login"))


@socketio.on("user_connected")
def user_connected():
    clients.append(request.sid)


@socketio.on("user_disconnect")
def user_disconnect():
    print(">> User disconnected {} ".format(request.sid))
    clients.remove(request.sid)


@socketio.on("command")
def command(cmd):
    global shell
    global process

    if cmd == "1":
        shell = Reader()
        process = shell.run()
        # shell._write(process, '1') # connected [1]
    elif cmd == "11":
        shell._write(process, "1")  # started [1]
    elif cmd == "2":
        shell._write(process, "2")  # stopped [2]
    elif cmd == "3":
        shell._write(process, "3")  # disconnect [3]


"""
    Reader
    Description:
"""
import threading, subprocess
from subprocess import Popen, PIPE


class Reader(object):
    PATH_BASE = str(pathlib.Path.cwd())

    reader_01 = 0
    reader_02 = 0
    reader_03 = 0
    reader_04 = 0
    reader_all_uniq = []

    def __init__(self):
        self.tag = mongo.db.tag
        self.log = mongo.db.log

    def run(self):
        # Error connecting to the reader (192.168.0.99) : Failed_A_Client_Initiated_Connection_Already_Exists
        # "192.168.0.99"
        #"192.168.0.97"
        # "10.19.3.68"

        args = [
            self.PATH_BASE + "/app/bin/impinj.jar",
            "192.168.0.97"
        ]

        process = subprocess.Popen(
            ["java", "-jar"] + list(args),
            encoding="utf-8",
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        def writeall(process):
            # cmd = ['connected', 'started', 'stopped', 'disconnect']

            while True:
                raw_data = process.stdout.readline()
                print(raw_data)
                
                raw_json = raw_data.replace("\\r\\n'", "")
                data_json = json.loads(raw_json)

                try:
                    if data_json["tag"]:
                        self.tag.insert(data_json)
                        self.reader_all_uniq.append(data_json["tag"])

                        if data_json["antenna"] == 1:
                            self.reader_01 += 1
                        elif data_json["antenna"] == 2:
                            self.reader_02 += 1
                        elif data_json["antenna"] == 3:
                            self.reader_03 += 1
                        elif data_json["antenna"] == 4:
                            self.reader_04 += 1

                        data_readers_counter = {
                            "reader_01": self.reader_01,
                            "reader_02": self.reader_02,
                            "reader_03": self.reader_03,
                            "reader_04": self.reader_04,
                            "reader_all_uniq": len(set(self.reader_all_uniq))
                        }

                        socketio.emit("readers_counter", data_readers_counter)

                        data_tags = {
                            "tag": data_json["tag"],
                            "time": data_json["time"]
                        }

                        socketio.emit("tags", data_tags)
                except KeyError:
                    self.log.insert(data_json)

                process.stdout.flush()

        writer = threading.Thread(target=writeall, args=(process,))
        writer.start()

        return process

    def _write(self, process, message):
        process.stdin.write(message + "\n")
        process.stdin.flush()
