

# Function to add a question
def add_question(questions):
    question_id = input("Enter question ID: ")
    if question_id in questions:
        print("Question ID already exists.")
        return
    question_text = input("Enter the question: ")
    options = []
    for i in range(4):
        options.append(input(f"Enter option {i + 1}: "))
    correct_answer = input("Enter the correct option number (1-4): ")
    questions[question_id] = {
        'question': question_text,
        'options': options,
        'answer': correct_answer
    }
    print("Question added successfully.")

# Function to view all questions
def view_questions(questions):
    for qid, qinfo in questions.items():
        print(f"ID: {qid}\nQuestion: {qinfo['question']}\nOptions: {', '.join(qinfo['options'])}\n")

# Function to delete a question
def delete_question(questions):
    question_id = input("Enter question ID to delete: ")
    if question_id in questions:
        confirm = input(f"Are you sure you want to delete question {question_id}? (Y/N): ")
        if confirm.lower() == 'y':
            del questions[question_id]
            print("Question deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Question ID not found.")

# Function to display the menu
def display_menu():
    print("\nQuiz Master Menu")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Delete Question")
    print("4. Exit")

# Function to display the quiz cracker menu
def display_quiz_cracker_menu():
    print("\nQuiz Cracker Menu")
    print("1. Take Quiz")
    print("2. Exit")

# Function to take the quiz
def take_quiz(questions, log):
    if not questions:
        print("No questions available. Please add questions first.")
        return
    score = 0
    for qid, qinfo in questions.items():
        print(f"ID: {qid}\nQuestion: {qinfo['question']}\nOptions:")
        for idx, option in enumerate(qinfo['options'], 1):
            print(f"{idx}. {option}")
        answer = input("Enter the correct option number (1-4): ")
        log.append((qid, answer == qinfo['answer']))
        if answer == qinfo['answer']:
            score += 1
    print(f"You scored {score}/{len(questions)}")
