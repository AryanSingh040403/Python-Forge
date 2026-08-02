age = int(input())

if age <= 0:
    print("Invalid Age")
elif age < 5:
    print("Free Entry")
elif age < 18:
    print("Ticket Price: ₹150")
elif age < 60:
    print("Ticket Price: ₹250")
else:
    print("Ticket Price: ₹180")
