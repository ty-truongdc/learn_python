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
			return(mileage)
		else:	return("You can not roll back the mileage.")
		
		
	def increment_odometer(self, miles):
		self.odometer_reading += miles
		return self.odometer_reading
class Battery:
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size = 75):
		"""Initialize the battery's attributes"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")

class Electric_Car(Car):
	"""Models aspects of a care, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()
						
