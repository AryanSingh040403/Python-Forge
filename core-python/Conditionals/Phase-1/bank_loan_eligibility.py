age = int(input())
sal = int(input())
cred_sc = int(input())
 # validation
if age < 0 or sal < 0 or (cred_sc < 0 or cred_sc > 850):   
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
if (age < 0) or (sal < 0) or not (0 <= cred_sc <= 850):   
    print("Invalid Input")
elif  21 <= age <= 60 and sal >= 25000 and cred_sc >= 700:    
    print("Loan Approved")
else:                                                  
    print("Loan Rejected")