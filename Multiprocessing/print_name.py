"""
Multiprocessing
"""
import concurrent.futures as cf
import time

def print_name(name):
    time.sleep(1)
    return f"Hello, {name}"

def main():
    """Main function"""
    with cf.ProcessPoolExecutor() as executor:
        names = ['honey', 'light', 'tanjiro', 'inosuke']
        results = executor.map(print_name, names)

        for result in results:
            print(result)

if __name__ == "__main__":
    main()