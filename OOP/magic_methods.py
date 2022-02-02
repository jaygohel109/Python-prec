"""
This is regarding magic/dunder methods
"""

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + "@company.com"
        self.pay = pay
        self.full_name = f"{first} {last}"

    def __repr__(self) -> str:
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self) -> str:
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee('honey', 'patel', 50000)
emp_2 = Employee('harsh', 'patel', 60000)

print(emp_1)
print(emp_2)

print(emp_1 + emp_2)
