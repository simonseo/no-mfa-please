#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: insert_user.py
# @Created:   2018-04-21 02:12:57  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-21 02:19:43  Simon Seo (simon.seo@nyu.edu)

import psycopg2
from .sql_config import get_config
from app.db import check_tables_exists
from app import app
from ..exceptions import UserDataNotFoundException

# @check_tables_exists
def get_user(email):
    """Retrieve user information that matches the given email"""
    app.logger.debug("User email address: {}".format(email))
    conn = None
    sql = """SELECT * FROM backup_mfa_accounts WHERE email LIKE %s;"""
    try:
        # read database configuration
        params = get_config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the SELECT statement
        app.logger.debug("Querying: {}".format(sql % email))
        cur.execute(sql, (email,))
        rows = cur.fetchall()
        app.logger.debug("fetched rows: {}".format(rows))
        for row in rows:
            app.logger.debug("each row: {}".format(row))
            return row
        # close communication with the database
        cur.close()
        conn.commit()
        app.logger.debug("No user was found with provided email")
        raise UserDataNotFoundException("No user was found with provided email")
    except (Exception, psycopg2.DatabaseError) as error:
        app.logger.debug("DB Exception in get_user: {}".format(error))
        raise error
    finally:
        if conn is not None:
            conn.close()
