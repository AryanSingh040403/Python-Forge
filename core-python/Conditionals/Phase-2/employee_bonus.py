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

years_of_experience = int(input())
performance_rating= int(input())

if years_of_experience < 0 or performance_rating < 1 or performance_rating > 5:
    print("Invalid Input")
elif years_of_experience >= 2:
    if performance_rating == 1 or performance_rating == 2:
        print("No Bonus")
    elif performance_rating == 5:
        print("20% Bonus")
    elif performance_rating == 4: 
        print("10% Bonus")
    else:
        print("5% Bonus")
else:
    print("No Bonus")
