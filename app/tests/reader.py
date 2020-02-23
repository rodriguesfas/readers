"""
    Software: Reader
    Description:
    Author: Team Cronos
    Data: 27/10/2019
    Version: 0.0.1
"""

import sys
import os
import subprocess
from subprocess import Popen, PIPE
import threading


class Reader(object):

    def __init__(self):
        pass

    def run(self):

        args = [
            "/home/fasr/Developer/Cronos/checkpoint/app/collector/bin/impinj.jar",
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
                    process.stdout.flush()

        writer = threading.Thread(target=writeall, args=(process,))
        writer.start()

        try:
            while True:
                d = input()
                if not d:
                    break
                self._write(process, d)

        except EOFError:
            pass

    def _write(self, process, message):
        process.stdin.write(message + "\n")
        process.stdin.flush()


shell = Reader()
shell.run()
