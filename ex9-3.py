"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.

Create several instances representing different users, and call both meth-
ods for each user.
"""
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def describe_user(self):
        print(f"User's name is {self.first_name} {self.last_name}")
        print(f"User is {self.age} years old")
        print(f"User's email is {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

user1 = User("Alice", "A", "alice@kiu.edu.ge", 18)
user2 = User("Bob", "B", "bob@kiu.edu.ge", 19)
user3 = User("Charlie", "C", "charlie@kiu.edu.ge", 20)

user1.describe_user()
user1.greet_user

user2.describe_user()
user2.greet_user

user3.describe_user()
user3.greet_user
