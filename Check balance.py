Balance =3000

print("1.Check Balance")
print("2.Deposite")
print("3.Withdraw")

Choice = int(input("Enter Your Choise:"))

if(Choice == 1):
    print("Current Balance =₹",Balance)

elif(Choice == 2):
    amount = float(input("Enter Deposite Amount:"))
    Balance = Balance+ amount
    print("Amount Deposited successfully")
    print("New Balance=₹",Balance)

elif(Choice == 3):
    amount = float(input("Enter Withdrawal amount:"))

    if(amount <= Balance):
        Balance = Balance-amount
        print("Withdrawal amount successfully")
        print("Remaining Balance=₹",Balance)
    else:
        print("Insufficiant Balance")

else:
    print("Wrong Choice")