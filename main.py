'''
Name:           main.py
Author:         Brian Richardson
Version:        1.1
Date:           July 7, 2021
Description:    This is the main file for lab08
'''

from flask import Flask, render_template, flash, redirect, request
from login import LoginForm, Config, RegistrationForm, UpdateForm
import functions
from functions import check_user_data

MESSAGE = "Default message"
CURRENT_USER = "none"
app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
@app.route("/main")
def main():
    '''
    Renders the 'main' web page
    '''
    # create moment instance for date and time
    datetime = functions.current_time()
    return render_template('main.html', datetime = datetime)

@app.route("/guide")
def guide():
    '''
    Renders the 'guide' web page
    '''
    posts = functions.guide_list()
    return render_template('guide.html', posts = posts)

@app.route("/links")
def links():
    '''
    Renders the 'links' web page
    '''
    links_list = functions.links_list()
    return render_template('links.html', posts = links_list)

@app.route("/registration", methods=['GET', 'POST'])
def registration():
    '''
    Renders the registration website
    '''
    global MESSAGE
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))

        # check to see if user exists
        if not functions.user_exists(form.username.data):
            # change the message
            MESSAGE = "Registered successfully"

            # store user data
            functions.store_user_data(form.username.data, form.password.data)
        else:
            MESSAGE = "Username already exists"

        return redirect('/result')
    return render_template('registration.html', title='Registration', form = form)

@app.route("/update", methods=['GET', 'POST'])
def update():
    '''
    Renders the update password page
    '''
    global MESSAGE, CURRENT_USER
    form = UpdateForm()
    if form.validate_on_submit():

        # if password exist, replace
        if check_user_data(CURRENT_USER, form.oldpassword.data):
            # replace passwords
            functions.replace_password(form.oldpassword.data, form.password2.data)
            MESSAGE = "Password changed"
        else:
            # forward to error page
            MESSAGE = "Unable to change password.  Please try again."
        return redirect('/result')
    return render_template('update.html', title='Update Password', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    '''
    Renders the 'login' web page
    '''
    global MESSAGE, CURRENT_USER
    form = LoginForm()

    # validate the form
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))

        # check login credentials
        if functions.check_user_data(form.username.data, form.password.data):
            MESSAGE = "User: "  + form.username.data
            CURRENT_USER = form.username.data
            return redirect('/userportal')
        else:
            MESSAGE = "User name or password is incorrect"
            functions.failed_log(form.username.data, request.remote_addr)
            return redirect('/result')
    return render_template('login.html', title='Sign In', form=form)

@app.route("/result")
def result():
    '''
    Renders the 'result' web page
    '''
    return render_template('result.html', message = MESSAGE)

@app.route("/userportal")
def user_portal():
    '''
    Renders the 'user
    '''
    return render_template('userportal.html', message = MESSAGE)
