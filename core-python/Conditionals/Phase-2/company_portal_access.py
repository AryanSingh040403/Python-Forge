Emp_ID = int(input())
status = input()
level = int(input())

if Emp_ID <= 0 or (status != "Active" and status != "Inactive") or level < 1 or level > 5:
    print("Invalid Input")
elif status == "Active":
    if level == 5:
        print("Full Access")
    elif level == 4 or level == 3:
        print("Limited Access")
    else:
        print("Access Denied")
else:
    print("Access Denied")


# better alternative:
if Emp_ID <= 0 or status not in ["Active", "Inactive"] or level < 1 or level > 5:
    print("Invalid Input")
elif status == "Active":
    if level == 5:
        print("Full Access")
    elif level >= 3:
        print("Limited Access")
    else:
        print("Access Denied")
else:
    print("Access Denied")