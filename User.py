#Bunquin, Theodore Von Joshua M.
#CS 1201

import random

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.points = 0

    def add_points(self, points):
        self.points += points

    def play_game(self):
        user_points = 0
        cpu_points = 0
        rounds = 0

        while user_points < 3 and cpu_points < 3:
            input("Press Enter to roll the dice.")
            user_roll = random.randint(1, 6)
            cpu_roll = random.randint(1, 6)

            print(f"You rolled: {user_roll}")
            print(f"CPU rolled: {cpu_roll}")

            if user_roll > cpu_roll:
                user_points += 1
                print("You won this round!")
            elif cpu_roll > user_roll:
                cpu_points += 1
                print("CPU won this round!")
            else:
                print("It's a tie!")

            rounds += 1

        if user_points >= 3:
            self.add_points(3)
            print(f"\nCongratulations! You won this game in {rounds} rounds.")
        else:
            print(f"\nSorry! CPU won this game in {rounds} rounds.")
