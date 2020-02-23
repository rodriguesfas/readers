"""
    Reader
    Description:
"""

import os, pathlib, threading, subprocess

from subprocess import Popen, PIPE

class Reader(object):

    HOME = os.environ['HOME']
    PATH_BASE = str(pathlib.Path.cwd())
    
    def __init__(self):
        pass
        #self.tag = mongo.db.tag

    def run(self):

        args = [
            self.PATH_BASE + "/app/bin/impinj.jar",
            "192.168.0.99",
        ]

        process = subprocess.Popen(
            ["java", "-jar"] + list(args),
            encoding="utf-8",
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        def writeall(process):
            while True:
                # print("read data: ")
                data = process.stdout.readline()
                if data:
                    print(data)
                    #self.tag.insert(data)
                    process.stdout.flush()

        writer = threading.Thread(target=writeall, args=(process,))
        writer.start()

        return process

    def _write(self, process, message):
        process.stdin.write(message + "\n")
        process.stdin.flush()