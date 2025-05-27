name = input("What is your name? ")
name_1 = name.capitalize()
print(f"Hello {name_1}! Welcome to Essay Buddy. ")

sentence = input("Enter a sentence from your hw. ")
if sentence != sentence.capitalize() :
    print("Your sentence should start with a capital letter. ") 
else:
    print("Nice! Good start!")
if (".") not in sentence :
    print("Don't forget to end your sentence with a full stop")
else:
    print("Nice! You ended your sentence properly.")

sentence.count("and")
print(f"You used \"and\" {int} times")
sentence.count("but")
print(f"You used \"but\" {int} times")
sentence_1 = sentence.split()
print(len(sentence_1))
sentence_2 = sentence.strip()
sentence_3 = sentence.isalpha()
if sentence_3 == True :
    print("Your sentence is clean, no strange characters.")
else:
    print("Your sentence has some special characters, clean it up!")

finale = print("Essay checked successfully!")
finale_2 = finale.center()