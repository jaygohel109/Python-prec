"""
Multithreading
"""
import concurrent.futures as cf
import time

def print_name(name):
    time.sleep(1)
    return f"Hello, {name}"

with cf.ThreadPoolExecutor() as executor:
    names = ['honey', 'light', 'tanjiro', 'inosuke']
    results = executor.map(print_name, names)

    for result in results:
        print(result)
