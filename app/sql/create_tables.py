#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: create_tables.py
# @Created:   2018-04-17 14:10:08  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-20 15:08:23  Simon Seo (simon.seo@nyu.edu)

import psycopg2
from app.sql.sql_config import config


def create_tables():
	""" create tables in the PostgreSQL database"""
	commands = (
		"""
			CREATE TABLE accounts (
			 user_id serial PRIMARY KEY,
			 -- username VARCHAR (50) UNIQUE NOT NULL,
			 password VARCHAR (50) NOT NULL,
			 email VARCHAR (355) UNIQUE NOT NULL,
			 -- created_on TIMESTAMP NOT NULL,
			 -- last_login TIMESTAMP
			 hotp_secret CHAR (32) NOT NULL -- looks like a85adc3516351791c05ef40bde772c24
			);
		""",)
	conn = None
	try:
		# read the connection parameters
		params = config()
		# connect to the PostgreSQL server
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		# create table one by one
		for command in commands:
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
