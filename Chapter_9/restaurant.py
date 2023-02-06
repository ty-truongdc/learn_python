#Creating a class called Restaurant   """*5\\ttempt to create simple class"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(restaurant_name, cuisine_type)

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")
		
class IceCreamStand(Restaurant):
	"""Attempt to create a child class"""
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		
	def display_flavor(self, flavor):
		print("Available flavor are:")
		for i in flavor:
			print(i.title(), end = " ")	

my_restaurant = Restaurant("Asian King", "Chinese Cuisine")
print(f"Restaurant name is: {my_restaurant.restaurant_name} and we serve {my_restaurant.cuisine_type}")
my_restaurant.open_restaurant()


ice_cream_flavor_list = ['strawberries', 'vanilla', 'blueberries', 'chocolate']		
my_icream_stand = IceCreamStand(ice_cream_flavor_list)
my_icream_stand = IceCreamStand('Luna', 'Viet Flavor')
my_icream_stand = Restaurant("Ice Cold", "Sweet")


print(my_icream_stand.describe_restaurant())
my_icream_stand.display_flavor(ice_cream_flavor_list)
