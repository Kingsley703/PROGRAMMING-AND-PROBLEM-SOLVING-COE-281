#Checking Usernames
current_users = ['Louis','Argon','Kingsley','baffoe','fione']
new_users = ['Argon','Kingsley','gloria','vida','saxe']
for user in new_users:
	if user in current_users:
		print(f"The person will need to enter a new username")
	else:
		print(f"The username is available")


#FizzBuzz
for num in range(1,101):
	if num % 3 == 0 and num % 5 == 0:
		print("Fizz")

	elif num % 5 == 0:
		print("Buzz")

	else:
		print(num)
