#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: ping.py
# @Created:   2018-04-17 02:46:57  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-17 02:47:44  Simon Seo (simon.seo@nyu.edu)
import os
from decorators import async

@async
def ping(hostname):
	response = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")
	return response