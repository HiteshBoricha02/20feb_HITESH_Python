# quiz_master.py

questions_file = 'C:\Full Stack\Back End\Python sanket Sir\Assessment\questions.txt'

# Load existing questions from file
def load_questions():
    questions = {}
   
    with open(questions_file, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 4:
                    qid = int(parts[0])
                    question_text = parts[1]
                    options = parts[2].split(',')
                    answer = parts[3]
                    questions[qid] = {
                        'question': question_text,
                        'options': options,
                        'answer': answer
                    }
    
    return questions

# Save questions to file
def save_questions(questions):
    with open(questions_file, 'w') as f:
        for qid, qdata in questions.items():
            options = ','.join(qdata['options'])
            line = f"{qid}|{qdata['question']}|{options}|{qdata['answer']}\n"
            f.write(line)

# Add a new question
def add_question(questions):
    question_id = len(questions) + 1
    question_text = input("Enter question: ")
    option1 = input("Enter option 1: ")
    option2 = input("Enter option 2: ")
    correct_answer = input("Enter correct answer: ")

    questions[question_id] = {
        'question': question_text,
        'options': [option1, option2],
        'answer': correct_answer
    }

    save_questions(questions)
    print("Question added successfully.")

# View all questions
def view_questions(questions):
    for qid, qdata in questions.items():
        print(f"ID: {qid}, Question: {qdata['question']}")
        for i, opt in enumerate(qdata['options'], start=1):
            print(f"Option {i}: {opt}")
        print(f"Correct Answer: {qdata['answer']}\n")

# Delete a question
def delete_question(questions):
    question_id = int(input("Enter question ID to delete: "))
    if question_id in questions:
        confirm = input("Are you sure you want to delete this question? (Y/N): ")
        if confirm.lower() == 'y':
            del questions[question_id]
            save_questions(questions)
            print("Question deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Question ID not found.")

def menu():
    questions = load_questions()

    while True:
        print("\nWELCOME MASTER")
        print("SHAKE YOUR BRAIN AND ADD SOME CHALLENGING QUESTIONS..")
        print("MENU")
        print("press 1 for add questions")
        print("press 2 for view questions")
        print("press 3 for delete questions")
        print("press 4 for exit")

        choice = input("Which operation do you want to perform: ")

        if choice == '1':
            add_question(questions)
        elif choice == '2':
            view_questions(questions)
        elif choice == '3':
            delete_question(questions)
        elif choice == '4':
            break
        else:
            print("Invalid input, please enter a number between 1 and 4.")
