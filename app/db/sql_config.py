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

local_config = {
	"host" : "127.0.0.1",
	"port" : 5432,
	"dbname" : "postgres",
	"sslmode" : 'prefer',
}

heroku_config = {
	"user" : db_url.split('://')[1].split(':')[0],
	"password" : db_url.split(':')[2].split('@')[0],
	"host" : db_url.split('@')[1].split(':')[0],
	"port" : int(db_url.split(':')[-1].split('/')[0]),
	"dbname" : db_url.split('/')[-1],
	"sslmode" : 'require',
}

def get_config():
	if on_local:
		app.logger.debug("config: {}".format(local_config))
		return local_config
	elif on_heroku:
		app.logger.debug("config: {}".format(heroku_config))
		return heroku_config
	else:
		raise Exception("Unknown environment; Neither Heroku or Local")
