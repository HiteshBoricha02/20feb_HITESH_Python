# quiz_cracker.py

questions_file = 'questions.txt'

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
   

def play_quiz():
    questions = load_questions()

    if not questions:
        print("No questions available. Please ask the Quiz Master to add some questions.")
        return

    correct_count = 0
    for qid, qdata in questions.items():
        print(f"\nQuestion: {qdata['question']}")
        for i, opt in enumerate(qdata['options'], start=1):
            print(f"Option {i}: {opt}")

        answer = input("Enter your answer: ")
        if answer.strip().lower() == qdata['answer'].strip().lower():
            print("Correct!")
            correct_count += 1
        else:
            print(f"Wrong! The correct answer is: {qdata['answer']}")

    print(f"\nYou got {correct_count} out of {len(questions)} questions correct.")

if __name__ == "__main__":
    play_quiz()
