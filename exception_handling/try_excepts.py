"""
Try, except, else, finally
"""

def main():
    """Main function"""

    try:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
    except ValueError:
        print("Please enter an integer value")
    else:
        result = a + b
        print(f"{a} + {b} = {result}")
    finally:
        print("I'll always run!")

if __name__ == '__main__':
    main()