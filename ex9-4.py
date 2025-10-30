"""
9-4. Number Served: Start with your program from Exercise 9-1.
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business.
"""
class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, restaurant_name: str, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summery of restaurant."""
        msg = f"{self.restaurant_name} serves wonderful {self.cuisine_type}"
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.restaurant_name} is open."
        print(f"\n{msg}")
    
    def set_number_served(self, number : int):
        if number < 0: 
            print("Number of people shouldn't be negative!") 
        else:
            self.number_served =  number

    def increment_number_served(self, number : int):
        if number < 0:
            print("Increment shouldn't be negative!")
        else:
            self.number_served += number

restaurant = Restaurant("Name", "Georgian")
print(f"default: {restaurant.number_served}")

restaurant.number_served = 5
print(f"direct: {restaurant.number_served}")

restaurant.set_number_served(25)
print(f"set_number_served: {restaurant.number_served}")

restaurant.increment_number_served(15)
print(f"increment_number_served: {restaurant.number_served}")
