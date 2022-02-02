"""
classmethods and staticmethod properties
"""

class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.email = fname.lower() + "." + lname.lower() + "@company.com" 
        self.pay = int(pay)

        Employee.num_of_emp += 1

    def full_name(self):
        return (f"{self.fname} {self.lname}")

    def apply_raise(self):
        self.pay *= self.raise_amount

    @classmethod
    def set_rais(cls, amount):
        cls.raise_amount =amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else: return True

emp_1 = Employee.from_string('honey-patel-50000')
print(emp_1.__dict__)

import datetime
sample_date = datetime.datetime(2022, 2, 5)
print(Employee.is_workday(sample_date))
