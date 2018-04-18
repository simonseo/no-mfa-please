#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: ping.py
# @Created:   2018-04-17 02:46:57  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-18 18:16:16  Simon Seo (simon.seo@nyu.edu)
import os
from app.decorators import async

@async
def ping(hostname):
	# hostname = "https://{}.herokuapp.com/".format(os.environ['HEROKU_APP_NAME'])
	response = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")
	return response
