#Re do restaurant.py for sake of practice.
#Create Restaurant class

class Restaurant:
	"""Attempt to create a class named Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
		#Add an attribute called 'flavor' containing a list of ice-cream flavors.

		self.flavors = ['strawberry', 'chocolate', 'blueberry', 'vanilla', 'pina-cona']
		
	#Make a method to print out the above information
	
	def describe_restaurant(self):
		print(f"The restaurant name is {self.restaurant_name} and we serve {self.cuisine_type}.")
		
	#Make another method to print a message that the restaurant is open.
	
	def open_restaurant(self):
		print(f"{self.restaurant_name} is open.")
		
	#Adding a method to update number of customers served.
	
	def increment_number_served(self, person):
		self.number_served += person
		return (self.number_served)

#Create a child class called IceCreamStand:

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)	
		self.flavor = ['strawberry','blueberry', 'chocolate', 'vanilla','pina-coda']

	#Create a method called 'display_flavor' to display all ice cream flavors.

	def display_flavors(self):
		print("We serve the following flavors:")
		for i in self.flavor:
			print(i.title())
		

#Make an instance called restaurant.

restaurant = Restaurant("cava".title(), "mexican cuisine".title())
print(restaurant.restaurant_name, restaurant.cuisine_type)

#Call the two above methods.

restaurant.describe_restaurant()
restaurant.open_restaurant()

#print number of customer served using instance:

print(f'The number {restaurant.restaurant_name} has served so far: {restaurant.number_served}.')

#print number of customer served using assigned number to instance:

restaurant.number_served = 24

print(f'The number {restaurant.restaurant_name} has served so far: {restaurant.number_served}.')

#print number of customer served using update method.

#First, ask user input how many customer served to add on:

how_many_served_today = int(input("How many customers did you have today?\n"))

print(f'The number {restaurant.restaurant_name} has served so far is {restaurant.increment_number_served(how_many_served_today)}')

#Make two more instances (two more restaurants).

second_restaurant = Restaurant("chipotle".title(), "local mexican cuisine".title())
third_restaurant = Restaurant("huong viet".title(), "vietnamese food".title())

#Call the above two methods again:

second_restaurant.describe_restaurant()
second_restaurant.open_restaurant()

third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()

#Create an instance for child class IceCreamStand.

IceCreamStand = IceCreamStand('sunshine'.title(),'everything creamy'.title())
IceCreamStand.describe_restaurant()
(IceCreamStand.display_flavors())