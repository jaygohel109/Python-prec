import pytest
from your_module import nth_fibonacci  # Replace 'your_module' with the actual name of your python file containing the nth_fibonacci function

def test_fibonacci_positive():
    # Testing positive cases
    assert nth_fibonacci(1) == 0, "The 1st Fibonacci number should be 0"
    assert nth_fibonacci(2) == 1, "The 2nd Fibonacci number should be 1"
    assert nth_fibonacci(3) == 1, "The 3rd Fibonacci number should be 1"
    assert nth_fibonacci(4) == 2, "The 4th Fibonacci number should be 2"
    assert nth_fibonacci(5) == 3, "The 5th Fibonacci number should be 3"
    assert nth_fibonacci(6) == 5, "The 6th Fibonacci number should be 5"
    # Add more tests as needed

def test_fibonacci_edge_case():
    # Testing edge cases
    assert nth_fibonacci(10) == 34, "The 10th Fibonacci number should be 34"
    # Add more edge cases as needed

def test_fibonacci_invalid():
    # Testing for invalid input
    with pytest.raises(ValueError):
        nth_fibonacci(0)
    with pytest.raises(ValueError):
        nth_fibonacci(-1)
    # Add more invalid inputs as needed

# Add more test functions as required
