# ==============================================================================
# RUNGTA INTERNATIONAL SKILLS UNIVERSITY
# SCHOOL OF COMPUTER SCIENCE AND ENGINEERING
# Bachelor of Technology Computer Science and Engineering
#
# PS No.: 7
# Project Title: Quiz Application
# Concepts Used: Lists, Dictionaries, Loops, Random module, Functions
# ==============================================================================

import random
import sys

# Question bank containing 12 multiple-choice questions
# (Exceeds the bare minimum requirement of 10 questions)
# Stored as a list of dictionaries with 'question', 'options', and 'answer'
question_bank = [
    {
        "question": "Keyword to define a function?",
        "options": {"A": "func", "B": "def", "C": "function", "D": "lambda"},
        "answer": "B"
    },
    {
        "question": 'len("Hi") = ?',
        "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
        "answer": "B"
    },
    {
        "question": "Mutable type?",
        "options": {"A": "tuple", "B": "str", "C": "list", "D": "int"},
        "answer": "C"
    },
    {
        "question": "Which symbol is used for single-line comments in Python?",
        "options": {"A": "//", "B": "/*", "C": "#", "D": "--"},
        "answer": "C"
    },
    {
        "question": "What is the output of 3 * 2 ** 2?",
        "options": {"A": "36", "B": "12", "C": "24", "D": "16"},
        "answer": "B"
    },
    {
        "question": "Which data type does not allow duplicate elements?",
        "options": {"A": "list", "B": "tuple", "C": "set", "D": "dictionary"},
        "answer": "C"
    },
    {
        "question": "Which method is used to add an item to the end of a list?",
        "options": {"A": "push()", "B": "append()", "C": "insert()", "D": "add()"},
        "answer": "B"
    },
    {
        "question": "What is the correct file extension for Python source files?",
        "options": {"A": ".pt", "B": ".pyt", "C": ".py", "D": ".python"},
        "answer": "C"
    },
    {
        "question": "What will type(5 / 2) return in Python 3?",
        "options": {"A": "int", "B": "float", "C": "double", "D": "number"},
        "answer": "B"
    },
    {
        "question": "Which keyword is used for loops in Python?",
        "options": {"A": "for", "B": "repeat", "C": "loop", "D": "iterate"},
        "answer": "A"
    },
    {
        "question": "What does range(3) produce when iterated?",
        "options": {"A": "0, 1, 2", "B": "1, 2, 3", "C": "0, 1, 2, 3", "D": "1, 2"},
        "answer": "A"
    },
    {
        "question": "Which operator is used for exponentiation (power) in Python?",
        "options": {"A": "^", "B": "**", "C": "//", "D": "%"},
        "answer": "B"
    }
]


def ask_question(q_num, q_data, pre_answer=None):
    """
    Displays a single multiple-choice question and its options,
    then prompts the user until a valid option (A, B, C, or D) is entered.
    If an invalid option is entered, notifies user and re-asks the question.
    """
    # If an answer was already provided at the startup prompt
    if pre_answer is not None and pre_answer in ["A", "B", "C", "D"]:
        print(f"\nQ{q_num}: {q_data['question']}")
        for opt, text in q_data["options"].items():
            print(f"  {opt} {text}")
        return pre_answer

    # Input validation loop: accepts only A, B, C, or D (case-insensitive)
    while True:
        print(f"\nQ{q_num}: {q_data['question']}")
        for opt, text in q_data["options"].items():
            print(f"  {opt} {text}")
        
        user_input = input("Enter your answer (A, B, C or D): ").strip().upper()
        if user_input in ["A", "B", "C", "D"]:
            return user_input
        print("Invalid option. Enter A, B, C or D.")


def run_quiz(questions, first_answer=None):
    """
    Runs the quiz for a given list of questions, tracks the score,
    prints feedback for each question, and displays the final evaluation.
    """
    score = 0
    total = len(questions)

    for i, q_data in enumerate(questions, start=1):
        # Use first_answer for Q1 if one was passed in, otherwise None
        pre_ans = first_answer if i == 1 else None
        user_ans = ask_question(i, q_data, pre_answer=pre_ans)

        # Check user's answer against the correct answer
        if user_ans == q_data["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Q{i} Wrong. Correct answer: {q_data['answer']}")

    # Calculate percentage and pass/fail status (Pass mark is 50%)
    percentage = (score / total) * 100
    result = "Pass" if percentage >= 50.0 else "Fail"

    # Display final score summary
    print("\n" + "=" * 45)
    print(f"Score: {score}/{total} | Percentage: {percentage:.2f}% | Result: {result}")

    # If the user fails, display the correct answers list
    if result == "Fail":
        correct_answers_list = [q["answer"] for q in questions]
        print(f"Correct answers: {', '.join(correct_answers_list)}")
    print("=" * 45)


def main():
    """
    Main function to handle mode selection:
    1. CLI flags: --random / -r (random questions) or --test / -t (test cases)
    2. Piped input: automatically runs evaluation test mode (Q1-Q3)
    3. Interactive console: lets user choose test mode or random mode
    """
    # Check command-line flags
    if len(sys.argv) > 1:
        flag = sys.argv[1].lower()
        if flag in ["--random", "-r", "random"]:
            print("\n[Random Quiz Mode] Selecting 5 questions randomly using random module...")
            selected_questions = random.sample(question_bank, 5)
            run_quiz(selected_questions)
            return
        elif flag in ["--test", "-t", "test"]:
            # Run the 3 standard benchmark test questions
            run_quiz(question_bank[:3])
            return

    # Check if input is piped from a file/test script
    if not sys.stdin.isatty():
        run_quiz(question_bank[:3])
        return

    # Interactive console menu
    print("=" * 55)
    print("         PYTHON CONSOLE QUIZ APPLICATION")
    print("   Rungta International Skills University (RISU)")
    print("=" * 55)
    print("Available Modes:")
    print("  [Enter] -> Run Evaluation Test Mode (Q1 to Q3)")
    print("  [R]     -> Run Random Quiz Mode (Random 5 from Bank)")
    print("-" * 55)

    mode_choice = input("Select mode (Press Enter for Test Mode, or 'R' for Random): ").strip().upper()

    if mode_choice == "R":
        print("\n[Random Quiz Mode] Selecting 5 questions randomly using random module...")
        selected_questions = random.sample(question_bank, 5)
        run_quiz(selected_questions)
    elif mode_choice in ["A", "B", "C", "D"]:
        # If user directly started answering Q1
        run_quiz(question_bank[:3], first_answer=mode_choice)
    else:
        # Default: Evaluation test mode (Q1-Q3)
        run_quiz(question_bank[:3])


if __name__ == "__main__":
    main()
