#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: sql_config.py
# @Created:   2018-04-17 14:14:28  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-18 19:10:56  Simon Seo (simon.seo@nyu.edu)
import os
from app import app

on_heroku = 'DYNO' in os.environ
on_local = not on_heroku # Is there a better way of checking if environment is local
db_url = os.environ['DATABASE_URL']

def get_config():

	if on_local:
		config = {
			"host" : "127.0.0.1",
			"port" : 5432,
			"dbname" : "postgres",
			"sslmode" : 'prefer',
		}
		app.logger.debug("config: {}".format(config))
		return config

	elif on_heroku:
		config = {
			"user" : db_url.split('://')[1].split(':')[0],
			"password" : db_url.split(':')[1].split('@')[0],
			"host" : db_url.split('@')[1].split(':')[0],
			"port" : int(db_url.split(':')[-1].split('/')[0]),
			"dbname" : db_url.split('/')[-1],
			"sslmode" : 'require',
		}
		app.logger.debug("config: {}".format(config))
		return config
		
	else:
		raise Exception("Unknown environment; Neither Heroku or Local")
