#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @File Name: form.py
# @Created:   2018-04-17 01:53:32  Simon Myunggun Seo (simon.seo@nyu.edu) 
# @Updated:   2018-04-21 03:19:27  Simon Seo (simon.seo@nyu.edu)

from wtforms import Form, BooleanField, StringField, PasswordField, SelectField, validators

class RegistrationForm(Form):
    qr_url = StringField('URL of QR Code image', [
            validators.DataRequired(),
            # validators.Regexp(regex, flags=0, message=None),
            validators.URL(require_tld=True, message='Doesn\'t look like a valid URL. It might be missing \'http://\' or \'.com\'')
        ],
        description='Something')
    email = StringField('Email Address', [
            validators.DataRequired(),
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
            validators.Email(message='Please enter a proper email address')
        ])
    password = PasswordField('Password', [validators.DataRequired()])
    count = SelectField('Number of passcodes to generate', 
        [validators.DataRequired()], 
        choices=[
            ('1', '1'),
            ('3', '3'),
            ('5', '5'),
            ('10', '10')
        ])
