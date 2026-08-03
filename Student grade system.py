name = input("Enter Student Name: ")

m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))
m4 = int(input("Enter Marks 4: "))
m5 = int(input("Enter Marks 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

print("Total =", total)
print("Percentage =", per)

if per >= 75:
    print("Grade = Distinction")
elif per >= 60:
    print("Grade = First Class")
elif per >= 40:
    print("Grade = Pass")
else:
    print("Grade = Fail")