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
		Function to save a newly created user instance
		'''
		# global users_list
		UserCredential.credentials_array.append(self)
	
# 	# def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
# 	# 	'''
# 	# 	Function to generate an 8 character password for a credential
# 	# 	'''
# 	# 	gen_pass=''.join(random.choice(char) for _ in range(size))
# 	# 	return gen_pass
	@classmethod
	def find_my_name(cls, account_name):
		for site in cls.credentials_array:
			if site.site_name == account_name:
				return site
		return False
	@classmethod
	def display_usercredentials(cls,user_name):
		'''
		Class method to display the list of credentials saved
		'''
		user_credentials_array = []
		for credential in cls.credentials_array:
			if credential.user_name == user_name:
				user_credentials_array.append(credential)
		return user_credentials_array

	def delete_credentials(self):
		UserCredential.user_credentials_array.remove(self)
				

	
	@classmethod
	def search_by_site_name(cls, site_name):
		'''
		Method that takes in a site_name and returns a credential that matches that site_name.
		'''
		for credential in cls.credentials_array:
			if credential.site_name == site_name:
				return credential

				
	@classmethod
	def page_exists(cls, pager):
		for pagy in cls.credentials_array:
			if pagy.site_name == pager:
				return pagy
		return False

# 	# @classmethod
# 	# def copy_credential(cls,site_name):
# 	# 	'''
# 	# 	Class method that copies a credential's info after the credential's site name is entered
# 	# 	'''
# 	# 	find_credential = Credential.find_by_site_name(site_name)
# 	# 	return pyperclip.copy(find_credential.password)

