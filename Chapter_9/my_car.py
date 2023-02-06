#Practice creating a class
class Car:
	"""Create a Car class"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		#self.color = 'red'
		#self.vin_number = 456
		
	def describe_car(self):
		
		return(f'My car make is:{self.make}\nModel is: {self.model}\nYear is: {self.year}')
		
	def more_car_desription(self):
		name = input("What's your name?")
		color = input("What's the color of your car?\n")
		vin_number = int(input("What's the mileage?\n"))
		return(f"{name.title()}'s car color is {color.title()} and the Vin Number\\ is {vin_number}")
		
#Create an instance my_car

my_car = Car('acura'.title(), 'rdx'.title(), 2020)
print(my_car.describe_car())
print(my_car.more_car_desription())

#Create an instance of your car.

your_car = Car('honda'.title(), 'civic'.title(), 2008)
print(your_car.describe_car())
print(your_car.more_car_desription())
