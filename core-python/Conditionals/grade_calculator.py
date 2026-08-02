marks = int(input())

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks >= 60 and marks <= 69:
    print("Grade D")
else:
    print("Grade F")




# more Cleaner Alternative:

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")