class Account:
    """Account class"""
    def __init__(self, balance):
        self.balance = balance

    def add_amount(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError

    def subtract_amount(self, amount):
        if amount > 0 and self.balance > amount:
            self.balance -= amount
        else:
            raise ValueError

# bal1 = Account(5000)
# bal1.add_amount(1000)
# print(bal1.balance)