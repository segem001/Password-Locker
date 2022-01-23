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
