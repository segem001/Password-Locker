# import pyperclip
# import random
# import string

# Global Variables
global users_array 
class UserDetails:
	'''
	Class to create user accounts and save their information
	'''
	# Class Variables
	# global users_list
	users_array = []
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_userdetails(self):
		'''
		Function to save a newly created user instance
		'''
		UserDetails.users_array.append(self)
	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in UserDetails.users_array:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

		class UserCredential:
	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	# Class Variables
	credentials_array =[]
	user_credentials_array = []
	# @classmethod
	# def check_user(cls,first_name,password):
	# 	'''
	# 	Method that checks if the name and password entered match entries in the users_list
	# 	'''
	# 	current_user = ''
	# 	for user in UserDetails.users_array:
	# 		if (UserDetails.first_name == first_name and UserDetails.password == password):
	# 			current_user = user.first_name
	# 	return current_user

	def __init__(self,user_name,site_name,account_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

	def save_usercredentials(self):
		'''