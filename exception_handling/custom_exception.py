"""
User defined exceptions
"""

class CustomError(Exception):
    """This is an user defined exception"""

    def __init__(self, age: int) -> None:
        self.age = age
        self.message = f"Please come after {18 - self.age} year(s)"
        super().__init__(self.message)

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise CustomError(age)
    else:
        print("Enjoy your day, sir!")
except ValueError:
    print("Please enter a valid age!")
except CustomError as e:
    print(e)
