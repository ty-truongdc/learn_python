#Create an instance called my_restaurant
from restaurant_module import Restaurant

my_restaurant = Restaurant("huong viet", "vietnamese food")
#Calling method from the module
print(my_restaurant.get_desription())

#Calling another method to say the restaurant is open
print(my_restaurant.open_restaurant())