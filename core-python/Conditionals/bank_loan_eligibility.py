# Validation Rules

# If any input is invalid, print:

# Invalid Input

# An input is invalid if:

# Age < 0
# Salary < 0
# Credit Score < 0
# Credit Score > 850


age = int(input())
sal = int(input())
cred_sc = int(input())
 # validation
if (age < 0) or (sal < 0) or (cred_sc < 0 or cred_sc > 850):   
    print("Invalid Input")
# Eligibility
elif age >= 21 and age <= 60 and sal >= 25000 and cred_sc >= 700:    
    print("Loan Approved")
# Rejection
else:                                                  
    print("Loan Rejected")


age = int(input())
sal = int(input())
cred_sc = int(input())
if (age < 0) or (sal < 0) or ( 0 <= cred_sc <= 850):   
    print("Invalid Input")
elif  21 <= age <= 60 and sal >= 25000 and cred_sc >= 700:    
    print("Loan Approved")
else:                                                  
    print("Loan Rejected")

# Eligibility Rules

# A customer is eligible only if all the following conditions are satisfied:

# Age is between 21 and 60 (inclusive).
# Salary is ₹25,000 or more.
# Credit Score is 700 or above.