"""
Try, except, else, finally
"""

from decimal import DivisionByZero


def main():
    """Main function"""

    try:
        try:
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
        except ValueError:
            print("Please enter an integer value")
        else:
            result = a / b
    except ZeroDivisionError:
        print("Can't be divided by zero")
    else:
        print(f"{a} / {b} = {result}")
    finally:
        print("I'll always run!")

if __name__ == '__main__':
    main()