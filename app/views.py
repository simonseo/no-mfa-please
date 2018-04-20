#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: views.py
# @Created:   2018-04-17 00:09:27  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-21 01:14:28  Simon Seo (simon.seo@nyu.edu)
from flask import request, render_template, redirect, url_for, flash

# Built-in
import os
import logging

# Private Libs
import psycopg2

# My own
from app.form import RegistrationForm, PasscodeRequestForm
from app import app

logger = logging.getLogger(__name__)
@app.route("/")#, methods=['GET','POST'])
def main():
	return '''
	<!doctype html>
	<title>Input new </title>
	<h1>Upload new File</h1>
	'''

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']
    # your code
    # return a response
    # 

@app.route('/register', methods=['GET', 'POST'])
def register_account():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # db.add(form.username.data, form.email.data, form.password.data)
        flash('Thanks for registering. Received {} {}'.format(form.email.data, form.password.data))
        return redirect(url_for('generate_passcode'))
    return render_template('register.html', title='Register New Account', form=form)

@app.route('/passcode', methods=['GET', 'POST'])
def generate_passcode():
    form = PasscodeRequestForm(request.form)
    if request.method == 'POST' and form.validate(): 
        # checking account info should ideally happen in form.validate
        # send email
        logger.debug("form validated")
        flash('We\'ll send an email to {0} with your new passcode! Received {0} {1} {2}'.format(form.email.data, form.password.data, form.count.data))
        return redirect(url_for('generate_passcode'))
    return render_template('generate-passcode.html', title='Generate Passcode', form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete_account():
    form = DeleteAccountForm(request.form)
    if request.method == 'POST' and form.validate():
        return redirect(url_for("register_account"))
    return render_template('delete.html', title='Delete Account Information', form=form)

@app.route('/edit', methods=['GET', 'POST'])
def edit_account():
    form = EditAccountForm(request.form)
    if request.method == 'POST' and form.validate():
        return redirect(url_for("generate_passcode"))
    return render_template('edit.html', title='Update Account Information', form=form)



