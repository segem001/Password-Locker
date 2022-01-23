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


def main():
	print(' ')
	print('Hello! Welcome to Password Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(enter_newuser(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')
		elif short_code == 'li':
			print("-"*60)
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = confirm_user(first_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							password_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if password_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							# elif password_choice == 'gp':
							# 	password = generate_password()
							# 	break
							elif password_choice == 'ex':
								break
							else:
								print('Oops! Wrong option entered. Try again.')
						save_credential(define_credential(user_name,site_name,account_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the site name for the credential password to copy: ')
						copy_credential(chosen_site)
						print('')
					else:
						print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
			print("-"*60)
			print(' ')
			print('Oops! Wrong option entered. Try again.')
				






if __name__ == '__main__':
	main()


