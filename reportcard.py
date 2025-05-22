full_name = input("What is your full name? ")
grade = input("What grade are you in? ")
subject_1 = input("What is your first subject? ")
subject_2 = input("What is your second subject? ")
subject_3 = input("What is your third subject? ")
mark_1 = input(f"What is the mark for {subject_1}? ")
mark_2 = input(f"What is the mark for {subject_2}? ")
mark_3 = input(f"What is the mark for {subject_3}? ")

print("--------------------------------------------")
print(f"\\\\\n VIRTUAL REPORT CARD")
print(f"\\\\\n NAME: {full_name}")
print(f"\\\\\n GRADE: {grade}")
print(f"\\\\\n {subject_1} = {mark_1}")
print(f"\\\\\n {subject_2} = {mark_2}")
print(f"\\\\\n {subject_3} = {mark_3}")

if [mark_1, mark_2, mark_3] in range(85,100) :
    print(f"Well done {full_name[ :7]}")

if [mark_1,mark_2,mark_3] in range(60,84) :
    print("It's alright, could be better.")

if [mark_1,mark_2,mark_3] in range(0,59)  :
    print("Not good enough!")

print("---------------------------------------------")