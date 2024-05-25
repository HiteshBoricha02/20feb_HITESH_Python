# quiz_game.py

import quiz_master

questions = {}  
log = []  

def main():
    while True:
        print("\nMain Menu")
        print("1. Quiz Master")
        print("2. Quiz Cracker")
        print("3. Exit")
        main_choice = input("Enter your choice (1-3): ")
        
        if main_choice == '1':
            while True:
                quiz_master.display_menu()
                choice = input("Enter your choice (1-4): ")
                
                if choice == '1':
                    quiz_master.add_question(questions)
                elif choice == '2':
                    quiz_master.view_questions(questions)
                elif choice == '3':
                    quiz_master.delete_question(questions)
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif main_choice == '2':
            while True:
                quiz_master.display_quiz_cracker_menu()
                choice = input("Enter your choice (1-2): ")
                
                if choice == '1':
                    quiz_master.take_quiz(questions, log)
                elif choice == '2':
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        elif main_choice == '3':
            print("Exiting the Quiz Game...")
            break
        
        else:
            print("Invalid choice. Please try again.")

main()
