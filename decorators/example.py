"""Decorators"""

def decorator_func(original_func):
    def wrapper_func():
        print(f"Wrapper function executed this before {original_func.__name__}")
        return original_func()
    return wrapper_func

@decorator_func
def display():
    print("Display function ran!")

display()