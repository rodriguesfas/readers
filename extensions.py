#!/usr/bin/env python
# -*- coding: utf-8 -*-
# extensions.py

from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask_socketio import SocketIO, emit

bcrypt = Bcrypt()
mongo = PyMongo()
socketio = SocketIO()