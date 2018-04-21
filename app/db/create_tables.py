#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: create_tables.py
# @Created:   2018-04-17 14:10:08  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-21 02:52:09  Simon Seo (simon.seo@nyu.edu)

import psycopg2
from app.db.sql_config import config
import logging
logger = logging.getLogger(__name__)

def create_tables():
	""" create tables in the PostgreSQL database"""
	logger.debug("Creating backup_mfa_accounts tables")
	commands = (
		"""
		CREATE TABLE backup_mfa_accounts (
			user_id SERIAL PRIMARY KEY,
			-- username VARCHAR (50) UNIQUE NOT NULL,
			email VARCHAR (355) UNIQUE NOT NULL,
			password VARCHAR (50) NOT NULL,
			-- created_on TIMESTAMP NOT NULL,
			-- last_login TIMESTAMP
			hotp_secret CHAR (32) NOT NULL, -- looks like a85adc3516351791c05ef40bde772c24
			counter INTEGER DEFAULT 0
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
			if command.strip(): # only execute non-empty ones
				cur.execute(command)
		# close communication with the PostgreSQL database server
		cur.close()
		# commit the changes
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		logger.error(error)
	finally:
		if conn is not None:
			conn.close()


if __name__ == '__main__':
	create_tables()
