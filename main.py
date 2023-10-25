# Mariyah Reynolds

def print_menu():
	# This function prints the menu
	print('Menu\n'
		  '-------------\n'
		  '1. Encode\n'
		  '2. Decode\n'
		  '3. Quit\n')

def encode(user_string):
	""" Updated to correctly return encoded string that moves
	each original number decimals string each up by 3
	:param user_string: password to be encoded
	:return: encoded password
	"""

	# Create empty string to store new password
	temp_password = ''

	# Iterate through user string
	for i in user_string:
		digit = int(i)
		# Handle digits that will not recount from 0
		if digit <= 6:
			digit += 3
			# Line 28: Change made after Benjamin's push to repository:
			temp_password += str(digit)
		# Handles digit that recount from 0 once
		# they reach 9
		elif digit > 6:
			# Line 32 - 36: Change made after Benjamin's push to repository:
			new_digit = 0
			for i in range(digit + 1):
				new_digit = int(i) - 7
			temp_password += str(new_digit)
			#(digit = count)  # note from Benjamin: the code starting "elif digit > 6:" to here
		# always results in "2". So an input user_password of 123456789 incorrectly encodes as
		# 123456222. Instead of "num in range", use "digit" to convert 7, 8,  and 9 to 0,
		# 1 and 2. "Count" is not needed.
	return temp_password


# Partner: You may write the decoder function here
def decode(new_password):
	"""# added by Benjamin to decode new_password using the lab's requirement of each digit being
	shifted up by 3 numbers. This will correctly decode when the encode(user_string) function
	is fixed.
	"""
	decoded = ""
	for i in new_password:
		if 3 <= int(i) <= 9:
			decoded += str(int(i) - 3)
		if 0 <= int(i) <= 2:
			decoded += str(int(i) + 7)
	return decoded


# Start of main function
if __name__ == '__main__':

	# Control when user exits
	while True:
		print_menu()

		# Prompt user for menu choice
		user_option = int(input('Please enter an option:'))

		if user_option == 1:
			# Prompt user for password
			user_password = input('Please enter your password to encode:')
			# Pass into encoder function
			new_password = encode(user_password)
			print('Your password has been encoded and stored!')
		elif user_option == 2:
			decoded = decode(new_password)  # added by Benjamin to call decode(new_password)
			# Line 80: Change made after Benjamin's push to repository:
			print(f'The encoded password is {new_password}, and the original password is {decoded}.')
		elif user_option == 3:
			break


