#Page 167

class Restaurant:
	def __init__(self,restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 35
		
	def describe_restaurant(self):
		return(f"The restaurant name is {self.restaurant_name.title()} and we served {self.cuisine_type.title()} food.")
		
	def open_restaurant(self):
		return(f"The restaurant is open.")
		
	def set_number_served(self):
		print(f"We have served {self.number_served} so far.")
		
	def increment_number_served(self, more_customer_served):
		if more_customer_served >= self.number_served:
			self.number_served += more_customer_served
		else: print("You can not lower the number of customers.")
		
	
		
		
restaurant = Restaurant('huong viet', 'viet')

print(restaurant.describe_restaurant())
print(restaurant.open_restaurant()) 

restaurant.number_served = 25
restaurant.increment_number_served(24)
restaurant.set_number_served()
