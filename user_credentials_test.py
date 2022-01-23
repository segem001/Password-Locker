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