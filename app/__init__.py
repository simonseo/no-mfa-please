#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: __init__.py
# @Created:   2018-04-17 02:46:15  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-17 14:29:45  Simon Seo (simon.seo@nyu.edu)
from flask import Flask
import os

app = Flask(__name__)

from app import views
