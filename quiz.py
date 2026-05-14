print("==== Python Quiz ====\n")
score = 0

answer1 = input("Q1: What is the capital of India? ").strip().lower()
if answer1 == "new delhi" or answer1 == "delhi":
    print("correct!")
    score += 1
else:
    print("Wrong answer: New Delhi")

answer2 = input("Q2: What does AI stands for? ").strip().lower()
if answer2 == "artificial intelligence":
    print("correct!")
    score += 1
else:
    print("Wrong answer: Artificial Intelligence")

answer3 = input("Q3: How many days in a week? ").strip().lower()
if answer3 == "7":
    print("correct!")
    score += 1
else:
    print("Wrong answer: 7")

answer4 = input("Q4: What is the new generation named as? ").strip().lower()
if answer4 == "genz":
    print("correct!")
    score += 1
else:
    print("Wrong answer: genz")

answer5 = input("Q5: what is the average height of men in India? ").strip()
if answer5 == "5'5" or answer5 == "165cm":
    print("correct!")
    score += 1
else:
    print("Wrong answer: 165cm")

print(f"\nYour score: {score}/5")
if score == 5:
    print("Perfect Score!")
elif score >4:
    print("Good Job!")
elif score >3:
    print("Good JOb!")
elif score >2:
    print("Keep Practicing!")
else:
    print("Keep Practicing!")
