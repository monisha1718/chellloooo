print("Welcome to the Computer & IT Basics Quiz")
print("Please answer each question by typing a, b, c, or d.\n")

score = 0

questions = [
    {
        "question": "1. Which device is considered the brain of the computer?",
        "A": "Hard Disk",
        "B": "Monitor",
        "C": "CPU",
        "D": "Keyboard",
        "Answer": "c"
    },
    {
        "question": "2. What does RAM stand for?",
        "A": "Random Access Memory",
        "B": "Read Access Memory",
        "C": "Rapid Action Memory",
        "D": "Run Access Mechanism",
        "Answer": "a"
    },
    {
        "question": "3. Which one is an output device?",
        "A": "Scanner",
        "B": "Keyboard",
        "C": "Printer",
        "D": "Mouse",
        "Answer": "c"
    },
    {
        "question": "4. What is the full form of URL?",
        "A": "Universal Resource Link",
        "B": "Uniform Resource Locator",
        "C": "Unified Retrieval Locator",
        "D": "Universal Retrieval Link",
        "Answer": "b"
    },
    {
        "question": "5. Which of the following is an example of an Operating System?",
        "A": "MS Word",
        "B": "Windows",
        "C": "Google Chrome",
        "D": "Adobe Reader",
        "Answer": "b"
    },
    {
        "question": "6. Which type of storage is permanent?",
        "A": "RAM",
        "B": "Cache",
        "C": "ROM",
        "D": "Registers",
        "Answer": "c"
    },
    {
        "question": "7. Which one is NOT a programming language?",
        "A": "Python",
        "B": "C++",
        "C": "Java",
        "D": "Microsoft Excel",
        "Answer": "d"
    },
    {
        "question": "8. Which protocol is used for sending emails?",
        "A": "HTTP",
        "B": "SMTP",
        "C": "FTP",
        "D": "TCP",
        "Answer": "b"
    },
    {
        "question": "9. What does 'www' stand for in a website address?",
        "A": "World Web Window",
        "B": "Wide Web World",
        "C": "World Wide Web",
        "D": "Web World Wide",
        "Answer": "c"
    },
    {
        "question": "10. Which unit is used to measure the processing speed of a CPU?",
        "A": "KB",
        "B": "Mbps",
        "C": "GHz",
        "D": "RPM",
        "Answer": "c"
    }
]

for q in questions:
    print("\n" + q["question"])
    print("a)", q["A"])
    print("b)", q["B"])
    print("c)", q["C"])
    print("d)", q["D"])
    
    user_ans = input("Your answer: ").lower()

    if user_ans == q["Answer"]:
        print("Correct.\n")
        score += 1
    else:
        print("Incorrect. Correct answer:", q["Answer"].upper(), "\n")

print("Quiz Completed.")
print("Your final score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent performance.")
elif score >= 7:
    print("Very good performance.")
elif score >= 4:
    print("Fair performance.")
else:
    print("Needs improvement.")
