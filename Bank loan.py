Salary=int(input("Enter Your Salary:₹"))
Credit_score=int(input("Enter Your Credite_Score:"))

if(Salary >= 30,000):
    if(Credit_score >= 750):
       print("Loan Approved")
    else:
       print("Loan rejected(Low Credit_Score)")   
else:
   print("Loan rejected(Low Salary)")
