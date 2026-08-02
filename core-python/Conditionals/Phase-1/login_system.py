username = input()
password = input()

if username == "admin" and password == "python123":
    print("Login Successful")
elif username != "admin" and password == "python123":
    print("Invalid Username")
else:  
    print("Invalid Password") # password != "python123":


# Better/cleaner alternative:
username = input()
password = input()

if username == "admin" and password == "python123":
    print("Login Successful")
elif username != "admin":
    print("Invalid Username")
else:
    print("Invalid Password")