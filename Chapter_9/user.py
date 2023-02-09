#Make a class called User with two attributes first_name and last_name:

class User:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.age = 0
		self.location = " "
		self.email = f'{first_name.lower()}.{last_name.lower()}@gmail.com'
		self.login_attemtp = 0
		
	def user_info(self):
		print (f'{self.first_name}, {self.last_name}, {self.age}, {self.email}')

	#Create method to inrement login attempt by 1

	def increment_login_attempts(self):
		self.login_attemtp += 1
		return (self.login_attemtp)

	#Create a method called 'reset_login_attempts' to reset the value of login
	#attempts to 0

	def reset_login_attempts(self):
		self.login_attemtp = 0
		return (self.login_attemtp)

		
user_1 = User("jonh".title(), "nguyen".title())
user_1.user_info()

#Checking the increment of login attempts.

print(user_1.increment_login_attempts())
print(user_1.increment_login_attempts())
print(user_1.increment_login_attempts())
print(user_1.increment_login_attempts())

#Testing method reset_login_attempts to see if log_in_attempts reset to 0

print(user_1.reset_login_attempts())


