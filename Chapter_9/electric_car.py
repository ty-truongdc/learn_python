class Car:
		
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		
		"""a simpple attempt to represent a car."""	
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
		
	def read_odometer(self):
		return("f(This car has {self.odometer_reading} miles on it.")
		
	def update_odometer(sefl, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can not roll back the odometer.")

	def increment_odometer(self, miles):
		self.odometer_reading += miles
		
	def fill_gas_tank(self, mile_read):
		if mile_read <= 35:
			return (f"Mileage reach {mile_read}, please fill your gas tank.")
		else:	return (f"Please fill gas tank when mileage read more than {mile_read}.")
my_car = Car("Acura", "MDX", 2008)
print(my_car.get_descriptive_name())
print(my_car.fill_gas_tank(36))

class Battery:
	"""A simple attempt to model a bettery for an electric car."""
	
	def __init__(self, battery_size = 75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size
		
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size} kWh battery.")
		
	def get_range(self):
		"""Print a statement about the range the battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
			
		print(f"This car can go about {range} miles on a full charge.")
		
	

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	
	def __init__(self, make, model, year):
		"""Initialize attributes of the parent class.
		Then initialize attritbutes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()
		self.battery_size = 75
		self.odometer_reading = 0
		
	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")
		
	def fill_gas_tank(self):
		"""Electric cars dont have gas tank"""
		print("This car doesn't need a gas tank.")
		
		
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

