"""Closure"""

def outer_func(msg):
    message = msg
    def inner_func(name):
        print(f"{msg}, {name}")
    
    return inner_func

hi_func = outer_func("Hi")
hello_func = outer_func("Hello")

hi_func('Honey')
hello_func('Tutvi')
    