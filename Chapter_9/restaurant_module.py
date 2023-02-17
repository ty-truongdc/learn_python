#Create a restaurant class and store it as a module.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    #Create a method to display restaurant info.
    def get_desription(self):
        long_name = f"{self.restaurant_name}, {self.cuisine_type}"
        return long_name.title()

    #Create another method to display the restaurant is open

    def open_restaurant(self):
        return (f"{self.restaurant_name.title()} is open now and we are serving {self.cuisine_type.title()}. Come on in!")

        