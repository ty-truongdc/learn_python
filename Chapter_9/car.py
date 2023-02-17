from car_main_class import Car
from car_main_class import Electric_Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
print(my_new_car.read_odometer())

print(my_new_car.update_odometer(2))
print(my_new_car.increment_odometer(45))

