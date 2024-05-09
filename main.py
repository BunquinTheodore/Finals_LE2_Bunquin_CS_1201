#Bunquin, Theodore Von Joshua M.
#CS 1201

from User_Manager import User_Manager

def main():
    user_manager = User_Manager()

    while True:
        print ("Welcome to the Dice Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            user_manager.register()
        elif choice == 2:
            user_manager.log_in()
            if user_manager.current_user:
                while True:
                    print("\n1. Start Game")
                    print("2. Show Top Scores")
                    print("3. Log Out")
                    inner_choice = int(input("Enter your choice: "))

                    if inner_choice == 1:
                        user_manager.current_user.play_game()
                    elif inner_choice == 2:
                        user_manager.show_top_scores()
                    elif inner_choice == 3:
                        user_manager.log_out()
                        break
                    else:
                        print("Invalid choice. Try again.")
        elif choice == 3:
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
