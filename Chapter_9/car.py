class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
		
	def read_odometer(self):
		return(f"This car has {self.odometer_reading} miles on it.")
	
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:	print("You can not roll back the mileage.")
		
	def increment_odometer(self, miles):
		self.odometer_reading += miles
				
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
my_new_car.update_odometer(35)
print(my_new_car.read_odometer())


your_old_car = Car('acura', 'mdx', 2008)
your_old_car.odometer_reading = 30
print(your_old_car.get_descriptive_name())
print(your_old_car.read_odometer())
print(my_new_car.read_odometer())
your_old_car.update_odometer(29)
print(your_old_car.read_odometer())


my_use_car = Car("subaru", "outback", 2010)
print(my_use_car.get_descriptive_name())
print(my_use_car.read_odometer())
my_use_car.update_odometer(30)
print(my_use_car.read_odometer())
my_use_car.increment_odometer(40)
print(my_use_car.read_odometer())

print("")
print(my_new_car.read_odometer())
print(your_old_car.read_odometer())
print(my_use_car.read_odometer())

