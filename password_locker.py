#! /usr/bin/env python3
# import pyperclip

from user_credentials import UserDetails, UserCredential

def enter_newuser(firstname,lastname,password):
	'''
	Function to create a new user account
	'''
	new_user = UserDetails(firstname,lastname,password)
	return new_user