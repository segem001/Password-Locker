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

	