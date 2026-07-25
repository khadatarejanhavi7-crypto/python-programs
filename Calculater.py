a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))

print("+" , "Addition")
print("-" , "Subtraction")
print("*" , "Multiplication")
print("/" , "Division")

choice=input("Enter your choice:")

if(choice=="+"):
    print("Addition=",a+b)
elif(choice=="-"):
    print("Subtraction=",a-b)
elif(choice=="*"):
    print("Multiplication=",a*b)
elif(choice=="/"):
    print("Division=",a/b)
else:
    print("Wrong choice")
     