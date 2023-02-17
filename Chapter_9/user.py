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

#Write a separate class called Privilages:
class Privileges:
	"""Store a list of privileges"""
	def __init__(self, privileges = ['can add post','can delete post', 'can ban user']):
		self.privileges = privileges

	def show_privileges(self):
		
		for privilege in self.privileges:
			print(privilege.capitalize())


	
		

#Create a child class call Admin to inherit the User class:

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)

		#Adding an attribute call 'privilleges' to store list of string:
		self.testing = Privileges()

	
		


"""		
user_1 = User("jonh".title(), "nguyen".title())
user_1.user_info()

#Checking the increment of login attempts.

print(user_1.increment_login_attempts())
print(user_1.increment_login_attempts())
print(user_1.increment_login_attempts())
print(user_1.increment_login_attempts())

#Testing method reset_login_attempts to see if log_in_attempts reset to 0

print(user_1.reset_login_attempts())
print("")
"""
boss = Admin('ty'.title(), 'truong'.title())
boss.user_info()

boss.testing.show_privileges()


