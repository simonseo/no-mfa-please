#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: flaskapp.py
# @Created:   2018-04-17 00:09:27  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-17 00:58:14  Simon Seo (simon.seo@nyu.edu)
from flask import Flask

app = Flask(__name__)

@app.route("/")#, methods=['GET','POST'])
def main():
	return '''
	<!doctype html>
	<title>Upload new File</title>
	<h1>Upload new File</h1>
	'''

if __name__ == "__main__":
	app.run()