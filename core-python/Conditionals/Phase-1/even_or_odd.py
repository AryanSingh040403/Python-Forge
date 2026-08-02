num = int(input("Enter num to check weather it's even or odd = "))

if num % 2 == 0:
    print("even")
else:
    print("odd")



# if you wanna treat zero as a special case, you can use the following code: 
num = int(input("Enter num to check wether it's even or odd = "))

if num == 0:
    print("zero")
elif num % 2 != 0:
    print("odd")
else:
    print("even")



