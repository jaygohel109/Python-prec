"""
Add two integers
"""

def add_int(num1, num2):
    if type(num1) != int or type(num2) != int:
        raise ValueError
    else:
        return num1 + num2