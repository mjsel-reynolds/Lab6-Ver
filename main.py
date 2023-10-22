# Mariyah Reynolds
# This is my github repository
# My main function and encoder function are below

# Feel free to add the decoder function where you see fit

def print_menu():
	# This function prints the menu
	print('Menu\n'
		  '-------------\n'
		  '1. Encode\n'
		  '2. Decode\n'
		  '3. Quit\n')

def encoder(user_string):
	# Take in 8-digit password in string format with only integers
	# Stores encoded password to new variable with each digit
	# shifted up by 3 numbers

	# Create empty string to store new password
	temp_password = ''

	# 12345555" -> '45678888'
	# Iterate through user string
	for i in user_string:
		digit = int(i)
		# Handle digits that will not recount from 0
		if digit <= 6:
			digit += 3
		# Handles digit that recount from 0 once
		# they reach 9
		elif digit > 6:
			count = 0
			for num in range(0,2):
				count += 1
			digit = count
		# Store encoded password to new variable
		temp_password += str(digit)
	return temp_password


# Partner: You may write the decoder function here
def decoder():
	pass


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
			new_password = encoder(user_password)
			print('Your password has been encoded and stored!')
		elif user_option == 2:
			pass
		elif user_option == 3:
			break


