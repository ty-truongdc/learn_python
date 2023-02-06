#Creating the Dog Class

class Dog:
    """Attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age


    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over.")
		
		
	def bark(self):
	if self.age > 4:
			print(f"{self.name} is old enough to bark.")
		else:
			print(f"{self.name} is too young to bark.")
	
	
my_dog = Dog('Willy', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} year old.")

my_dog.sit()
my_dog.roll_over() 

your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} year olds.")
your_dog.sit()

new_dog = Dog('Kiki', 5)
new_dog.bark()
another_dog = Dog('Yellow', 2)
another_dog.bark()
