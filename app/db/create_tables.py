#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: create_tables.py
# @Created:   2018-04-17 14:10:08  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-21 02:52:09  Simon Seo (simon.seo@nyu.edu)

import psycopg2
from app.db.sql_config import config


def create_tables():
	""" create tables in the PostgreSQL database"""
	with open('db_create.sql', 'r') as sqlfile:
		commands = sqlfile.read().split(';')
	conn = None
	try:
		# read the connection parameters
		params = config()
		# connect to the PostgreSQL server
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		# create table one by one
		for command in commands:
			if command.strip(): # only execute non-empty ones
				cur.execute(command)
		# close communication with the PostgreSQL database server
		cur.close()
		# commit the changes
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()


if __name__ == '__main__':
	create_tables()
