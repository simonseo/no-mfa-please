#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: decorators.py
# @Created:   2018-04-17 02:19:49  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-17 02:51:40  Simon Seo (simon.seo@nyu.edu)

import os
from threading import Thread

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

    