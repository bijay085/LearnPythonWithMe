#------------------> Very simple quiz game but using list-------------#
print("☣️ Welcome to Mini-project -Quiz 🧑‍💻. Answer with 'yes' or 'no' or provide the required output.")
score = 0
questions = [
    {"question": "Does Python have a 'do while' loop?", "answer": "no"},
    {"question": "Is Python case-sensitive?", "answer": "yes"},
    {"question": "How to convert any text to lowercase?", "answer": ".lower()"}
]

choice = input("Ready to play? Type 'y' for yes, 'n' for no: ").lower()

if choice == 'y':
    for q in questions:
        answer = input(q["question"] + "\n").lower()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer. The correct answer is:", q["answer"])

    print(f'Your score is {score}')

else:
    exit()
