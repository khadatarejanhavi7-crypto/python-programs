a = int(input("Enter First Number"))
b =int(input("Enter Second Number"))

print("+","Addition")
print("-","Substraction")
print("*","Multiplication")
print("/","Division")

Choice = input("Enter Your Choice:")

if(Choice == "+"):
   print("Addition=", a+b)

elif(Choice == "-"):
   print("Substraction=",a-b)

elif(Choice == "*"):
   print("Multiplication=",a*b)

elif(Choice == "/"):
   print("Division=",a/b)

else:
   print("Werong Choice")