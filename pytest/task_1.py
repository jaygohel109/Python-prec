"""
Task to perform a pytest
"""
import math

phi = ( 1 + math.sqrt(5) ) / 2
def nth_fibonacci(n):
    """Returns nth number in fibonacci"""
    if n <= 0:
        raise ValueError
    else:
        result = ( math.pow(phi, n) - math.pow( (1 - phi), n ) ) / math.sqrt(2)
        return int(result)
