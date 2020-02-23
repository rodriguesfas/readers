#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# run.py 

from flaskwebgui import FlaskUI
from app import app, socketio

def run_sock():
    # TODO Remover IP e Port daqui e colocar em um aqruivo de configuração.
    socketio.run(app, host="127.0.0.1", port=9998)

if __name__ == '__main__':
    ui = FlaskUI(server=run_sock, host="127.0.0.1", port=9998)
    ui.run()
    exit(0)