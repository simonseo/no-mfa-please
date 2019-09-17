#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: update_user.py

import psycopg2
from .sql_config import get_config
from app.db import check_tables_exists
import logging
logger = logging.getLogger(__name__)


@check_tables_exists
def update_user(uid, email=None, password=None, hotp_secret=None, counter=None):
    """update the user data"""
    # TODO Create query string
    sql = """UPDATE table_name
            SET column1 = value1, column2 = value2...., columnN = valueN
            WHERE [condition];"""
    conn = None
    try:
        params = get_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print("Querying: {}".format(sql % email))
        cur.execute(sql, (email, password))
        rows = cur.fetchall()
        exists = bool(rows)
        print(rows)
        print(list(rows))
        # close communication with the database
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
    finally:
        if conn is not None:
            conn.close()
        return exists
