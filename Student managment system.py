class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"

    def display(self):
        print("Name =", self.name)
        print("Marks =", self.marks)
        print("Grade =", self.calculate_grade())
        print("--------------------")

S1 = student("Ajay", 90)
S2 = student("Vijay", 60)

S1.display()
S2.display()