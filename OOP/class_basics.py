"""
Basics of OOP in python
"""

class Employee:

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = fname.lower() + "." + lname.lower() + "@company.com" 
        self.pay = pay

    def full_name(self):
        return (f"{self.fname} {self.lname}")

emp_1 = Employee('Honey', 'Patel', 50000)
emp_2 = Employee('Test', 'User', 60000)
 
print(emp_1.__dict__)
print(emp_2.__dict__)

print(Employee.full_name(emp_1))
print(Employee.full_name(emp_2))
