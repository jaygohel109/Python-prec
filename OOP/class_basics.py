"""
Basics of OOP in python
"""

class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = fname.lower() + "." + lname.lower() + "@company.com" 
        self.pay = pay

        Employee.num_of_emp += 1

    def full_name(self):
        return (f"{self.fname} {self.lname}")

    def apply_raise(self):
        self.pay *= self.raise_amount

emp_1 = Employee('Honey', 'Patel', 50000)
emp_2 = Employee('Test', 'User', 60000)
 
# print(emp_1.__dict__)
# print(emp_2.__dict__)

#print full names using a method
print(Employee.full_name(emp_1))
print(Employee.full_name(emp_2))

print("Total employees:", Employee.num_of_emp)

#initial values
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#change var for one instance
emp_1.raise_amount = 1.05

#applying raise and printing new pay
emp_1.apply_raise()
print(emp_1.pay)
