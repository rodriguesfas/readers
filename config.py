#!/usr/bin/env python
# -*- coding: utf-8 -*-
# config.py

import os, pathlib

class Config(object):
    PATH_BASE = str(pathlib.Path.cwd())
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    #HOME = os.environ['HOME']

    #BASE_URL = 'http://127.0.0.1:9999/'
    
    LANG = 'en'
    
    DEBUG = False
    TESTING = False
    
    # https://djecrety.ir/
    SECRET_KEY = 'jup=p2hv@yz&h7uk!hko$l&8*@ocj2p0beea@+1!7u!k$ku50s'
    
    MONGO_DBNAME = 'checkpoint'
    MONGO_URI = 'mongodb://localhost:27017/checkpoint'

    IMAGE_UPLOADS = BASE_DIR + "uploads"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    #HOME = os.environ['HOME']
    PATH_BASE = str(pathlib.Path.cwd())
    #BASE_URL = 'http://127.0.0.1:5000/'
    
    LANG = 'en'
    
    DEBUG = True
    
    # https://djecrety.ir/
    SECRET_KEY = 'vnkdjnfjknfl1232#'
    
    MONGO_DBNAME = 'checkpoint'
    MONGO_URI = 'mongodb://localhost:27017/checkpoint'

    IMAGE_UPLOADS = PATH_BASE + "uploads"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False