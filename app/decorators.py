#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: decorators.py
# @Created:   2018-04-17 02:19:49  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-20 15:11:24  Simon Seo (simon.seo@nyu.edu)

import os
from threading import Thread
from app.sql.create_tables import create_tables

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

def check_db_table_exists(f):
	def wrapper(*args, **kwargs):
		# somehow check that db and table exists
		f(*args, **kwargs)
	return wrapper





