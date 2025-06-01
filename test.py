import random
import time
import json

# Load questions from a JSON file
def load_questions(category):
    try:
        with open("quiz_questions.json", "r") as file:
            all_questions = json.load(file)
            return all_questions.get(category, [])
    except FileNotFoundError:
        print("Error: Questions file not found. Please create a quiz_questions.json file.")
        return []

# Ask user for a category
categories = ["general", "math", "science"]
print("Choose a category:", ", ".join(categories))
selected_category = input("Enter category: ").strip().lower()

if selected_category not in categories:
    print("Invalid category! Defaulting to 'general'.")
    selected_category = "general"

questions = load_questions(selected_category)
if not questions:
    print(f"No questions found for '{selected_category}'. Exiting quiz.")
    exit()

random.shuffle(questions)

score = 0
max_time = 10  # Time limit per question in seconds

print(f"\nStarting {selected_category.capitalize()} Quiz!\n")

# Loop through questions
for i, q in enumerate(questions):
    print(f"Question {i+1}: {q['question']}")
    for choice in q["choices"]:
        print(choice)

    # Timer starts
    start_time = time.time()
    user_answer = input("\nEnter your answer (A, B, C, or D): ").strip().upper()
    elapsed_time = time.time() - start_time

    # Check if time exceeded
    if elapsed_time > max_time:
        print("Time's up! No points for this question.\n")
        continue

    # Validate input
    if user_answer not in ["A", "B", "C", "D"]:
        print("Invalid input! Please enter A, B, C, or D.\n")
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

# Save high score
try:
    with open("scoreboard.json", "r") as file:
        scoreboard = json.load(file)
except FileNotFoundError:
    scoreboard = {}

scoreboard[selected_category] = max(scoreboard.get(selected_category, 0), score)

with open("scoreboard.json", "w") as file:
    json.dump(scoreboard, file)

print("\nCurrent High Scores:")
for category, best_score in scoreboard.items():
    print(f"{category.capitalize()}: {best_score}/{len(questions)}")
