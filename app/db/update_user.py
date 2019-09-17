#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: update_user.py

import psycopg2
from .sql_config import get_config
from app.db import check_tables_exists
from app import app

# @check_tables_exists
def update_user(uid, email=None, password=None, hotp_secret=None, counter=None):
    """update the user data"""
    # TODO Create query string
    sql = """UPDATE backup_mfa_accounts SET counter = %s WHERE user_id = %s;"""
    conn = None
    try:
        params = get_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        app.logger.debug("Querying: {}".format(sql.format(counter, uid)))
        cur.execute(sql, (counter, uid))
        # close communication with the database
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        app.logger.error(type(error), error)
        raise error
    finally:
        if conn is not None:
            conn.close()
