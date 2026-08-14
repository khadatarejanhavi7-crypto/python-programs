num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by Both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Neither Divisible by 3 nor 5")