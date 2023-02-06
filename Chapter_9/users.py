#Make a class called User.
number = 0
while number <=3:
	class User:
		def __init__(self, first_name, last_name):
			self.first_name = first_name
			self.last_name  = last_name
			self.login_attempt = 0
			
			
		def name_desription(self):
			print(f"First name is:\t{self.first_name.title()} \nLast name is: \t{self.last_name.title()}")
				
		def user_age(self,age):
			print(f"{self.first_name.title()} is {age} years old.")
					
		def location(self, location1):
			print(f"{self.first_name.title()} lives in {location1.title()}.")
			print("")
			
		def increment_login_attempts(self):
			self.login_attempt += 1
			print(f"You tried to log in {self.login_attempt} times")
			
		def reset_login_attempt(self):
		
			print(f"You have tried more than {self.login_attempt} times to log in.")
			self.login_attempt = 0
			print("Please try again in 5 minutes.")
			
	class Admin(User):
		
		def __init__(self, first_name, last_name):	
			
			super().__init__(first_name, last_name)
			
			self.privileges = ["can add post", "can delete post", "can ban user"]

		def admin_rights(self):
			
			for i in self.privileges:
				print(f"{self.first_name} {self.last_name} is the only person {i}.")
			return False
	first_user = User('ana', 'phan')
	first_user.name_desription()
	first_user.user_age(25)
	first_user.location("alexandria")
	first_user.increment_login_attempts()
	first_user.increment_login_attempts()
	first_user.increment_login_attempts()
	first_user.increment_login_attempts()
	first_user.reset_login_attempt()
	#if self.login_attempt > 4:
	#	first_user.reset_login_attempt()

	second_user = User('gabby', 'rojas')
	second_user.name_desription()
	second_user.user_age(22)
	second_user.location("Springfield")

	third_user = User('john', 'nguyen')
	third_user.name_desription()
	third_user.user_age(55)
	third_user.location("Annandale")
	
	number +=1
admin = Admin("Ty", "Truong")
admin.name_desription()
print(admin.admin_rights())
if admin.admin_rights():
	print("It is true.")
else:	print("False")