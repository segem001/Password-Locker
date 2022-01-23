#! /usr/bin/env python3
# import pyperclip

from user_credentials import UserDetails, UserCredential

def enter_newuser(firstname,lastname,password):
	'''
	Function to create a new user account
	'''
	new_user = UserDetails(firstname,lastname,password)
	return new_user
def save_user(user):
	'''
	Function to save a new user account
		'''
	UserDetails.save_userdetails(user)

def confirm_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	c = UserDetails.check_user(first_name,password)
	return c

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = UserCredential.generate_password()
	return gen_pass

def define_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=UserCredential(user_name,site_name,account_name,password)
	return new_credential

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return UserCredential.display_usercredentials(user_name)
	
