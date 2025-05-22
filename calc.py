import random

name = input("What's your name? ")
print(f"Welcome {name} to SmartCalc!")

operation = input("What operation would you like to perform? Add, Subtract, Division, Multiplication or Surprise? ")
stripped_operation = operation.strip()
operation_list = str("Add, Subtract, Division, Multiplication, Surprise")
if stripped_operation in operation_list :
 number_1 = int(input(f"Pick one number"))
 number_2 = int(input(f"Pick another number"))
 result_1 = int(number_1 + number_2)
 result_2 = int(number_1 - number_2)
 result_3 = int(number_1 * number_2)
 result_4 = int(number_1 / number_2)

 

 if stripped_operation == ("Add") :
  print(f"The sum of {number_1} + {number_2} is {result_1}")

 if stripped_operation == ("Subtract") :
  print(f"The sum of {number_1} - {number_2} is {result_2}")

 if stripped_operation == ("Multiplication") :
  print(f"The sum of {number_1} * {number_2} is {result_3}")

 if stripped_operation == ("Division") :
   print(f"The sum of {number_1} / {number_2} is {result_4}")


 if operation_list == ("Surprise") :
  correct_number = random.randint(1,10)
  guess = int(input("Guess the correct number"))
  if guess == correct_number :
   print("Well done!")
else :
   print("Error warning")




 


