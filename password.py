print("----------------------------")
print("SIGN UP")

username = input("What is your username? ")
password = input("What is your password? ")
password_2 = input("What is your password? ")
if password_2 == password :
    print("Account created successfully!")
else:
    print("Password doesnt't match, try again.")

print("----------------------------")

print("----------------------------")
print("LOG IN")

username_login = input("What is your username? ")
password_login = input("What is your password? ")
if username == username_login and password == password_login :
    print(f"Welcome back {username}! ")
else :
    print("Username and/or password is wrong, please try again.")

print("-----------------------------")