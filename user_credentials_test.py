import unittest
import pyperclip
from user_credentials import UserDetails , UserCredential

class TestUserDetails(unittest.TestCase):
	
	

	'''
	Test class that defines test cases for the user class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = UserDetails('Kiprono','Segem','123')


def test__init__(self):
	'''
	Test to if check the initialization/creation of user instances is properly done
	'''
	self.assertEqual(self.new_user.first_name,'Kiprono')
	self.assertEqual(self.new_user.last_name,'Segem')
	self.assertEqual(self.new_user.password,'123')

def test_save_userdetails(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_userdetails()
		self.assertEqual(len(UserDetails.users_array),1)
class TestUserCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''

	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = UserDetails('Kiprono','Segem','123')
		self.new_user.save_userdetails()
		user2 = UserDetails('davy','langat','123')
		user2. save_userdetails()

		for user in UserDetails.users_array:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

	self.assertEqual(current_user,UserCredential.check_user(user2.password,user2.first_name))

	def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = UserCredential('Kiprono','Facebook','Segem','123')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name,'Kiprono')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'Segem')
		self.assertEqual(self.new_credential.password,'123')

	def test_save_usercredentials(self):
		'''
		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_usercredentials()
		Facebook = UserCredential('Dominic','Myac','kiprono','123')
		Facebook.save_usercredentials()
		self.assertEqual(len(UserCredential.credentials_array),2)

# 	# def test_generate_password(self):
# 	# 	'''
# 	# 	Test to check if the generate password generates 8 character long alphanumeric numbers
# 	# 	'''
# 	# 	self.twitter = Credential('Twitter','maryjoe','')
# 	# 	self.twitter.password = generate_password()
# 	# 	self.assertEqual()

	def tearDown(self):
		'''
		Function to clear the credentials list after every test
		'''
		UserCredential.credentials_array = []
		UserDetails.users_array = []

	def test_display_usercredentials(self):
		'''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
		self.new_credential.save_usercredentials()
		Facebook = UserCredential('Kiprono','Myac','dominic','123')
		Facebook.save_usercredentials()
		gmail = UserCredential('kip','Gmail','dom','1234')
		gmail.save_usercredentials()
		self.assertEqual(len(UserCredential.display_usercredentials(Facebook.user_name)),2)

	def test_search_by_site_name(self):
		'''
		Test to check if the find_by_site_name method returns the correct credential
		'''
		self.new_credential.save_usercredentials()
		facebook = UserCredential('Kiprono','Facebook','Segem','123')
		facebook.save_usercredentials()
		credential_exists = UserCredential.search_by_site_name('Facebook')
		self.assertEqual(credential_exists.site_name,facebook.site_name)

# 	def test_copy_credential(self):
# 		'''
# 		Test to check if the copy a credential method copies the correct credential
# 		'''
# 		self.new_credential.save_credentials()
# 		twitter = Credential('Jane','Twitter','maryjoe','pswd100')
# 		twitter.save_credentials()
# 		find_credential = None
# 		for credential in Credential.user_credentials_list:
# 				find_credential =Credential.find_by_site_name(credential.site_name)
# 				return pyperclip.copy(find_credential.password)
# 		Credential.copy_credential(self.new_credential.site_name)
# 		self.assertEqual('pswd100',pyperclip.paste())
# 		print(pyperclip.paste())

if __name__ == '__main__':
	unittest.main(verbosity=2)