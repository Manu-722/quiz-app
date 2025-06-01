import random
import time

# Define the list of questions
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Where is Hyrax hills located?",
        "choices": ["A. Mombasa", "B. Nairobi", "C. Kisumu", "D. Nakuru"],
        "answer": "D"
    }
]

# Shuffle questions
random.shuffle(questions)

score = 0

print("Welcome to the CLI Quiz Game!\n")

# Loop through questions
for i, q in enumerate(questions):
    print(f"Question {i+1}: {q['question']}")
    for choice in q["choices"]:
        print(choice)

    # Timer (optional)
    start_time = time.time()
    user_answer = input("\nEnter your answer (A, B, C, or D): ").strip().upper()
    elapsed_time = time.time() - start_time

    # Validate input
    if user_answer not in ["A", "B", "C", "D"]:
        print("Invalid input! Please enter A, B, C, or D.")
        continue

    # Check answer
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect! The correct answer was {q['answer']}.\n")

# Provide feedback based on score
print(f"Your final score: {score}/{len(questions)}")

if score == len(questions):
    print("Excellent!")
elif score >= len(questions) // 2:
    print("Good job!")
else:
    print("Try again! Keep practicing.")
