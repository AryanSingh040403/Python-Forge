exp = int(input())
rat= int(input())

if exp < 0 or (rat < 1 or rat > 5):
    print("Invalid Input")
elif exp >= 2:
    if rat == 5:
        print("20% Bonus")
    elif rat == 4:
        print("10% Bonus")
    elif rat == 3: 
        print("5% Bonus")
    else:
        print("No Bonus")
else:
    print("No Bonus")



# better/Cleaner alternative:

