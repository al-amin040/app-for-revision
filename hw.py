import random

name = input("What is your name? ")
age = int(input ("What is your age? "))

if age < 14 :
    print("You're too young!")
else :
    print("Welcome, let's play!")




correct_number = random.randint(1,5)
guess = int(input("Guess the correct number? "))
if guess == correct_number:
    print("Well done!")
else:
    print("Unlucky!")
    guess = int(input("Guess the correct number? "))
    if guess == correct_number:
        print("Well done!")
    else:
        print("Unlucky, no more attempts!")



score = 0
one = random.randint(1,12)
two = random.randint(1,12)
user_answer = int(input(f"What is  {one} * {two}? "))
if user_answer == (one * two):
    print("Correct!")
    score = score + 1
else:
    print("Wrong, try again!")
user_answer2 = int(input(f"What is {one} + {two}? "))
if user_answer2 == (one + two):
    print("Correct!")
    score = score + 1
else:
    print("Unlucky, no more tries!")




x = 10
y = 12.5
z = True


answer_1 = input(f"What is {x}? ")
if answer_1 == "int":
    print(f"Correct!")
    score = score + 1
else:
    print(f"Incorrect! ")
answer_2 = input(f"What is {y}? ")
if answer_2 == "float" :
    print(f"Correct!")
    score = score + 1
else:
    print(f"Incorrect! ")
answer_3 = input(f"What is {z}? ")
if answer_3 == "bool" :
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

total_score = score


print(f"Well done {name}, you scored {total_score}/5.")
    




