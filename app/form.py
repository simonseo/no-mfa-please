#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: form.py
# @Created:   2018-04-17 01:53:32  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-20 15:26:40  Simon Seo (simon.seo@nyu.edu)

from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    qr_url = StringField('URL of QR Code image', [
        validators.DataRequired(),
        # validators.Regexp(regex, flags=0, message=None),
        validators.URL(require_tld=True, message='URL might be missing \'http://\' or \'.com\'')
    ])
    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.Length(min=6, max=35), 
        validators.Email(message='Please enter a proper email address')
    ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', [validators.DataRequired()])
    accept_tos = BooleanField('I accept the Terms of Service', [validators.DataRequired()])

class PasscodeRequestForm(Form):
    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.Length(min=6, max=35), 
        validators.Email(message='Please enter a proper email address')
    ])
    password = PasswordField('Password', [
        validators.DataRequired()
    ])
