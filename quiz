questions = ("how many", "what is", "why is", "where is", "is?")

options = (("A. 2", "B. 3", "C 5", "D 67"),
           ("A. a bird", "B. a plane", "C. a rock", "D. a potato"),
           ("A. why not?", "B. because", "C. well", "D. yeah"),
           ("A. Here", "B. there", "C. idk", "D. somewhere"),
           ("A. Yeah", "B. no", "C. perhaps", "D. maybe"))


answers = ("C", "D", "A", "B", "C")
guesses = []
score = 0
questionnum = 0

print("     Quiz Time!!!     ")

for question in questions:
    print("----------------------")
    print(question)
    for option in options[questionnum]:
        print(option)
    guess = input("Enter your Guess(A/B/C/D):  ").upper()
    guesses.append(guess)
    if guess == answers[questionnum]:
        score += 1
        print("Correct!!!")
    else:
        print(f"Incorrect!! {answers[questionnum]} is correct.")
    questionnum += 1


print("----------------------")
print("-------RESULTS!-------")
print("----------------------")
print(f"You got {score}/5 Correct!!")
if score == 5:
    print("Well done!!")
elif score == 4:
    print("Woah almost perfect!!")
elif score == 3:
    print("You did ok, better luck next time!!")
elif score == 2:
    print("Atleast its not 1")
elif score == 1:
    print(".. welp atleast you got one!")
else:
    print("... how bad can you possibly be? ")
