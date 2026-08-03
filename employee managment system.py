class Employee:
    def __init__(self, emp_id, name, department, salary, experience):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.experience = experience
    def bonus(self):
        if self.salary >= 50000:
            return self.salary + (self.salary * 0.20)
        elif self.salary >= 30000:
            return self.salary + (self.salary * 0.10)
        else:
            return self.salary + (self.salary * 0.05)
    def employee_status(self):
        if self.experience >= 5:
            return "Senior Employee"
        else:
            return "Junior Employee"
    def display(self):
        print("Employee ID :", self.emp_id)
        print("Employee Name :", self.name)
        print("Department :", self.department)
        print("Salary :", self.salary)
        print("Experience :", self.experience, "Years")
        print("Salary with Bonus :", self.bonus())
        print("Employee Status :", self.employee_status())
        print("--------------------------------")
E1 = Employee(101, "Rahul Sharma", "IT", 55000, 6)
E2 = Employee(102, "Priya Patil", "HR", 28000, 2)
E1.display()
E2.display()