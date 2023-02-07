#Re do restaurant.py for sake of practice.
#Create Restaurant class

class Restaurant:
	"""Attempt to create a class named Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	#Make a method to print out the above information
	
	def describe_restaurant(self):
		print(f"The restaurant name is {self.restaurant_name} and we serve {self.cuisine_type}.")
		
	#Make another method to print a message that the restaurant is open.
	
	def open_restaurant(self):
		print(f"{self.restaurant_name} is open.")
		
#Make an instance called restaurant.

restaurant = Restaurant("cava".title(), "mexican cuisine".title())

#Call the two above methods.

restaurant.describe_restaurant()
restaurant.open_restaurant()

#Make two more instances (two more restaurants).

second_restaurant = Restaurant("chipotle".title(), "local mexican cuisine".title())
third_restaurant = Restaurant("huong viet".title(), "vietnamese food".title())

#Call the above two methods again:

second_restaurant.describe_restaurant()
second_restaurant.open_restaurant()

third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()