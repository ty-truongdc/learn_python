class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def sit(self):
		print(f"{self.name} is sitting down.")
		
	def roll_over(self):
		print(f"{self.name} rolled over.")
		
	def bark(self):
		if self.age < 4:
			print(f"Your dog {self.name} is too young to bark.")
		else:
			print(f"Your dog {self.name} is old enough to bark.")
		
my_dog=Dog('Willi', 6)

print(f"My dog name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()
my_dog.bark()

your_dog = Dog('Lucy', 2)

print(f"Your dog name is {your_dog.name}.")
print(f"Your dog is {your_dog.age}.")

your_dog.sit()
your_dog.roll_over()
your_dog.bark()	

	