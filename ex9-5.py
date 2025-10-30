"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class
from Exercise 9-3. Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""


class User:
    """Represent a simple user profile."""

    def __init__(
        self, first_name: str, lasnt_name: str, username: str, email: str, location: str
    ):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = lasnt_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"[*] Username: {self.username}")
        print(f"[*] Email: {self.email}")
        print(f"[*] Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}")
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Name", "Last name", "Username", "email@example.com", "Kutaisi")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"login attempts : {user1.login_attempts}")

user1.reset_login_attempts()
print(f"reset: {user1.login_attempts}")