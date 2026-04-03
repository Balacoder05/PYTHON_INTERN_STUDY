questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Chennai", "B. Mumbai", "C. New Delhi", "D. Kolkata"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. HTML", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. Elon Musk", "D. Bill Gates"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! Correct answer is:", q["answer"])

print("\n🎉 Quiz Finished!")
print("Your Score:", score, "/", len(questions))