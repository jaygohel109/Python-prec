"""
Inheritence
"""

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + "." + last.lower() + "@company.com"
        self.pay = pay
        self.full_name = f"{first} {last}"

class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_emps(self):
        for emp in self.employees:
            print("--->", emp.full_name)

dev_1 = Developer('abc', 'xyz', 50000, 'Python')
mng = Manager('honey', 'patel', 90000, [dev_1])

mng.show_emps()
