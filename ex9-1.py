"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
"""
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}")
        print(f"This restaurant serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is open!!")

restaurant = Restaurant("New", "Georgian")

print(f"name of the restaurant: {restaurant.name}")
print(f"{restaurant.name} serves {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()