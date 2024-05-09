#Bunquin, Theodore Von Joshua M.
#CS 1201

from User import User
from Dice_Game import Dice_Game

class User_Manager:
    def __init__(self):
        self.users = []
        self.current_user = None
        self.load_users()

    def load_users(self):
        self.users = [
            User("user1", "password1"),
            User("user2", "password2")
        ]

    def validate_username(self, username):
        if len(username) >= 4:
            return True
        else:
            print("Username should have at least 4 characters.")
            return False

    def validate_password(self, password):
        if len(password) >= 6:
            return True
        else:
            print("Password should have at least 6 characters.")
            return False

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if self.validate_username(username) and self.validate_password(password):
            new_user = User(username, password)
            self.users.append(new_user)
            print("Registration successful.")

    def log_in(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print(f"Welcome, {user.username}!")
                return

        print("Invalid username or password.")

    def log_out(self):
        self.current_user = None
        print("Logged out successfully.")

    def show_top_scores(self):
        if self.current_user:
            dice_game = Dice_Game(self.current_user)
            dice_game.show_top_scores()
