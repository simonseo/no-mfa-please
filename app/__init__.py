#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: __init__.py
# @Created:   2018-04-17 02:46:15  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-17 02:49:33  Simon Seo (simon.seo@nyu.edu)
from flask import Flask
import os
import psycopg2

app = Flask(__name__)
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')