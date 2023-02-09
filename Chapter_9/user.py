#Make a class called User with two attributes first_name and last_name:

class User:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.age = 0
		self.location = " "
		self.email = f'{first_name}.{last_name}@gmail.com'
		
	def user_info(self):
		return (self.first_name, self.last_name, self.age, self.email)	
user_1 = ("jonh".title(), "nguyen".title())
print(user_1.user_info())