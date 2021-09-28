'''
Name:           functions.py
Author:         Brian Richardson
Version:        1.1
Date:           July 9, 2021
Description:    This is the function file for lab 08
'''
from datetime import datetime

def guide_list():
    '''
    Returns a dictionary of items for the guide ordered list
    '''
    items = [
        {'title':'The Roman Gods',
         'price':'$2.2 Billion',
         'image':'image01.jpg'},
        {'title':'Wooden Wu Prop',
         'price':'$104,500.95',
         'image':'image02.jpg'},
        {'title':'14K Gold C-3PO',
         'price':'$26,125.95',
         'image':'image03.jpg'},
        {'title':'Solid Silver C-3PO',
         'price':'$34,485.95',
         'image':'image04.jpg'},
    ]
    return items

def links_list():
    '''
    Returns a dictionary of items for links list
    '''
    links = [
        {'title': 'Brick Link',
         'url': 'https://www.bricklink.com/v2/main.page'},
        {'title': 'LEGO® Website',
         'url': 'https://www.lego.com'},
        {'title': 'LEGO® Laser Rifle',
         'url': 'https://www.youtube.com/watch?v=Gj7qGkIdQ4E'}
    ]
    return links

def current_time():
    '''
    Returns a string of the current date and time
    '''
    now = datetime.now() #current date and time

    date_time = {}

    date_time['date'] = now.strftime("%m/%d/%Y")
    date_time['time'] = now.strftime("%H:%M:%S")

    return date_time

def store_user_data(username, password):
    '''
    Takes a user name and password and writes it to users.txt
    '''
    # create a string
    user_data = username + " " + password + "\n"
    # open file
    with open('users', 'a') as file:
        file.writelines(user_data)

def user_exists(username):
    '''
    Checks if the user exists in users.txt
    '''
    # open file
    file = open("users", "r")

    # setting found and index
    found = False

    # Loop through the file line by line
    for line in file:

        # check if username is in line
        if username in line:
            found = True
            break
    file.close()
    return found

def check_user_data(username, password):
    '''
    Reads the users.txt and returns true if username and password match
    '''
    # open file
    file = open("users", 'r')
    # setting found and index
    found = False

    # Loop through the file line by line
    for line in file:
        # split the line into user data array
        user_data = line.split(" ")

        # check if username matches
        if username == user_data[0]:
            # check if the password matches
            if password == user_data[1].strip():
                found = True
                break
    file.close()
    return found

def build_password_list():
    '''
    Builds a common password array from CommonPassword.txt
    '''
    with open('CommonPassword.txt', 'r') as file:
        common_passwords = []

        # Loop through the file line by line
        for line in file:

            # add each line to an array
            common_passwords.append(line.strip())

    file.close()
    return common_passwords

def replace_password(old_password, new_password):
    '''
    Searches users file for the username and replaces the password
    '''
    with open('users', 'r') as file:
        # read file
        file_source = file.read()

        # replace old password with new password
        replace_string = file_source.replace(old_password, new_password)

        file.close()

    with open('users', 'w') as file:
        # write to file
        file.write(replace_string)
        file.close()

def failed_log(user_name, ip_address):
    '''
    Logs failed login attempts
    '''
    # get current time
    date_time = current_time()

    # create string
    log_line = user_name + ", " + ip_address + ", " + date_time['date'] + " - " + date_time['time'] + "\n"

    with open('log.txt', 'a') as log:
        log.write(log_line)
        log.close()
