#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: insert_user.py
# @Created:   2018-04-21 02:12:57  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-21 02:19:43  Simon Seo (simon.seo@nyu.edu)

import psycopg2
from .sql_config import get_config
from app.db import check_tables_exists
import logging
logger = logging.getLogger(__name__)


@check_tables_exists
def insert_user(email, password, hotp_secret, counter=0):
    """insert rows into the PostgreSQL database"""
    sql = """INSERT INTO backup_mfa_accounts (email, password, hotp_secret, counter) VALUES (%s, %s, %s, %s);"""
    conn = None
    try:
        # read database configuration
        params = get_config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        logger.debug("inserting using query: {}".format(sql % (email, password, hotp_secret, counter)))
        cur.execute(sql, (email, password, hotp_secret, counter,))
        # close communication with the database
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        raise error
    finally:
        if conn is not None:
            conn.close()
 
if __name__ == '__main__':
	insert_user('simon.seo@nyu.edu', 'asdf', 'a85adc3516351791c05ef40bde772c24')
