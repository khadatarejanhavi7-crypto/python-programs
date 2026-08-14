pin = input("Enter ATM PIN: ")
balance = 10000

if pin == "1234":
    amount = int(input("Enter Withdrawal Amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance = ₹", balance)
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")

