print("Vanakkam da pulla!")
print("Answer these questions by typing a, b, c, or d.\n")

score = 0

questions = [
    {
        "question": "1. Which of the following is a fermented South Indian dish?",
        "A": "Chapati",
        "B": "Dosa",
        "C": "Puri",
        "D": "Paratha",
        "Answer": "b"
    },
    {
        "question": "2. Which of the following dishes is traditionally made by fermenting rice and urad dal?",
        "A": "Pongal",
        "B": "Dosa",
        "C": "Rasam",
        "D": "Avial",
        "Answer": "b"
    },
    {
        "question": "3. \"Sambar\" is best described as:",
        "A": "A sweet dessert made of jaggery",
        "B": "A spicy lentil-based vegetable stew",
        "C": "A deep-fried snack",
        "D": "A type of flatbread",
        "Answer": "b"
    },
    {
        "question": "4. Which South Indian state is particularly famous for \"Hyderabadi Biryani\"?",
        "A": "Karnataka",
        "B": "Kerala",
        "C": "Andhra Pradesh / Telangana",
        "D": "Tamil Nadu",
        "Answer": "c"
    },
    {
        "question": "5. What is Idiyappam commonly known as?",
        "A": "Rice noodles",
        "B": "Sweet rice balls",
        "C": "Lentin pancake",
        "D": "Coconut fritters",
        "Answer": "a"
    },
    {
        "question": "6. Which ingredient is essential in Kerala’s famous dish ‘Puttu’?",
        "A": "Wheat flour",
        "B": "Rice flour",
        "C": "Millet",
        "D": "Semolina",
        "Answer": "b"
    },
    {
        "question": "7. ‘Appam’ is usually served with:",
        "A": "Sambar",
        "B": "Chicken stew or vegetable stew",
        "C": "Rasam",
        "D": "Pickle alone",
        "Answer": "b"
    },
    {
        "question": "8. What is the primary ingredient in “Avial”?",
        "A": "Fish",
        "B": "Mixed vegetables",
        "C": "Rice",
        "D": "Lentils",
        "Answer": "b"
    },
    {
        "question": "9. Which South Indian snack is a deep-fried lentil doughnut?",
        "A": "Murukku",
        "B": "Vada",
        "C": "Idli",
        "D": "Pathiri",
        "Answer": "b"
    },
    {
        "question": "10. “Bisi Bele Bath” is a specialty of which state?",
        "A": "Andhra Pradesh",
        "B": "Karnataka",
        "C": "Kerala",
        "D": "Tamil Nadu",
        "Answer": "b"
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
        print("Correct!\n")
        score += 1
    else:
        print("Wrong! Correct answer is:", q["Answer"].upper(), "\n")

print("Your final score:", score, "/", len(questions))
