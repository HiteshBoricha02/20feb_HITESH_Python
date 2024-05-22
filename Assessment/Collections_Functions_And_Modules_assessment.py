# quiz_game.py
import quiz_cracker
import quiz_master

def main_menu():
    while True:
        print("\nWELCOME TO TOPS QUIZ GAMING CHALLENGE")
        print("Select your role :")
        print("-> Quiz Master (press 1 )")
        print("-> Quiz Cracker (press 2 )")

        role = input("Enter your role: ")

        if role == '1':
            quiz_master.menu()
        elif role == '2':
            quiz_cracker.play_quiz()
        else:
            print("Invalid input, please enter 1 or 2.")
            

if __name__ == "__main__":
    main_menu()
