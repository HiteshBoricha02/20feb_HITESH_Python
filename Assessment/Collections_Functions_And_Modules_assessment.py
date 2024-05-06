# Function to load questions from a file
def load_questions():
    try:
        with open("questions.txt", "r") as file:
            lines = file.readlines()
            questions = {}
            for line in lines:
                q_id, question, option1, option2, option3, option4, answer = line.strip().split(",")
                questions[int(q_id)] = {"question": question, "options": [option1, option2, option3, option4], "answer": answer}
    except FileNotFoundError:
        questions = {}
    
    return questions

# Function to save questions to a file
def save_questions(questions):
    with open("questions.txt", "w") as file:
        for q_id, q_details in questions.items():
            options = ",".join(q_details["options"])
            file.write("{},{},{},{}\n".format(q_id, q_details["question"], options, q_details["answer"]))

# Function for Quiz Master to add a question
def add_question(questions):
    question = input("Enter the question: ")
    options = [input("Enter option {}: ".format(chr(97+i))) for i in range(4)]
    answer = input("Enter the correct option (a, b, c, d): ").lower()
    questions[len(questions) + 1] = {"question": question, "options": options, "answer": answer}
    save_questions(questions)
    print("Question added successfully.")

# Function for Quiz Master to view all questions
def view_questions(questions):
    if not questions:
        print("No questions available.")
    else:
        for q_id, q_details in questions.items():
            print("Question {}: {}".format(q_id, q_details["question"]))
            print("Options:")
            for i, option in enumerate(q_details["options"]):
                print("{}. {}".format(chr(97+i), option))
            print("Answer: ", q_details["answer"])
            print()

# Function for Quiz Master to delete a question
def delete_question(questions):
    question_id = int(input("Enter the question ID to delete: "))
    if question_id in questions:
        confirmation = input("Are you sure you want to delete this question? (Y/N): ").lower()
        if confirmation == "y":
            del questions[question_id]
            save_questions(questions)
            print("Question deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Question ID not found.")

# Function for Quiz Cracker to view questions and answer them
def quiz_cracker(questions):
    if not questions:
        print("No questions available.")
    else:
        for q_id, q_details in questions.items():
            print("Question {}: {}".format(q_id, q_details["question"]))
            print("Options:")
            for i, option in enumerate(q_details["options"]):
                print("{}. {}".format(chr(97+i), option))
            answer = input("Enter your answer (a, b, c, d): ").lower()
            if answer == q_details["answer"]:
                print("Correct!")
            else:
                print("Incorrect. The correct answer is: ", q_details["answer"])
            print()

# Main function
def main():
    print("Welcome to Quiz Game!")
    questions = load_questions()

    while True:
        print("\nMenu:")
        print("1. Quiz Master - Add Question")
        print("2. Quiz Master - View Questions")
        print("3. Quiz Master - Delete Question")
        print("4. Quiz Cracker - View and Answer Questions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_question(questions)
        elif choice == "2":
            view_questions(questions)
        elif choice == "3":
            delete_question(questions)
        elif choice == "4":
            quiz_cracker(questions)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    main()
