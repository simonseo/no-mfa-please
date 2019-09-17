#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: sql_config.py
# @Created:   2018-04-17 14:14:28  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-18 19:10:56  Simon Seo (simon.seo@nyu.edu)
import os
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_config():
	on_heroku = 'DYNO' in os.environ
	on_local = not on_heroku # Is there a better way of checking if environment is local
	if on_local:
		return {
			"host" : "127.0.0.1",
			"port" : 5432,
			"dbname" : "postgres",
		}
	elif on_heroku:
		config = {
			"user" : os.environ['DATABASE_URL'].split('://')[1].split(':')[0],
			"password" : os.environ['DATABASE_URL'].split(':')[1].split('@')[0],
			"host" : os.environ['DATABASE_URL'].split('@')[1].split(':')[0],
			"port" : int(os.environ['DATABASE_URL'].split(':')[-1].split('/')[0]),
			"dbname" : os.environ['DATABASE_URL'].split('/')[-1],
			"sslmode" : 'require',
		}
		logger.debug("config: {}".format(config))
		return config
	else:
		raise Exception("Unknown environment; Neither Heroku or Local")
