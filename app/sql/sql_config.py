#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: sql_config.py
# @Created:   2018-04-17 14:14:28  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-18 19:10:56  Simon Seo (simon.seo@nyu.edu)
import os

def config():
	on_heroku = 'DYNO' in os.environ
	on_local = not on_heroku
	if on_local:
		return {
			"host" : "127.0.0.1",
			"port" : 5432,
			"dbname" : "postgres",
		}
	elif on_heroku:
		return {
			"host" : os.environ['DATABASE_URL'],
			"sslmode" : 'require'
		}
	else:
		raise Exception("Unknown environment; Neither Heroku or Local")
