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
	self.new_user = UserDetai