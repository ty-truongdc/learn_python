from car_main_class import Electric_Car
my_tesla = Electric_Car('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()