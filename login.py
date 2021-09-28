'''
Name:           login.py
Author:         Brian Richardson
Version:        1.1
Date:           July 7, 2021
Description:    This file contains functions and classes for managing user logins and registration
'''
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from werkzeug.routing import ValidationError
import functions

class Config(object):
    '''
    Configuration class for forms
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess-the-key'

class LoginForm(FlaskForm):
    '''
    Login form class
    '''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField('Login')

def common():
    '''
    Custom validator for common passwords
    '''
    def _common(form, field):
        common_passwords = functions.build_password_list()
        word = field.data
        if word in common_passwords:
            raise ValidationError("Password must not be a commonly used password")
    return _common

def secure():
    '''
    Custom validator for secure passwords
    '''
    def _secure(form, field):

        special = ['!','@','#', '$', '%', '^', '*', '(',')']
        word = field.data
        if not any(char.isdigit() for char in word):
            raise ValidationError("Password must contain at least 1 number")
        if not any(char.isupper() for char in word):
            raise ValidationError("Password must contain at least 1 capital letter")
        if not any(char.islower() for char in word):
            raise ValidationError("Password must contain at least 1 lowercase letter")
        if not any(char in special for char in word):
            raise ValidationError("Password must contain at least 1 symbol")
    return _secure

class RegistrationForm(FlaskForm):
    '''
    Registration form class
    '''
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=100)])
    password = PasswordField('Password', validators=[DataRequired(),
                            Length(min=12, max = 32), secure(), common()])
    submit = SubmitField('Register')

class UpdateForm(FlaskForm):
    '''
    Update password form class
    '''
    match_message = "Passwords must match"
    oldpassword = PasswordField('Old Password', validators=[DataRequired()])
    password1 = PasswordField('New Password', validators=[DataRequired(),
                            Length(min=12, max=32), common(), secure()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(),
                            Length(min=12, max = 32), EqualTo('password1', match_message)])
    submit = SubmitField('Change Password')
