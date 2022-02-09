"""
Test file for task 1
"""

import pytest
from task_1 import nth_fibonacci

@pytest.mark.parametrize('nth_fibonacci, num', [(1, 1), (2, 1), (3, 2), (4, 3)])
def test_value(nth_fibonacci, num):
    assert nth_fibonacci(nth_fibonacci) == num

@pytest.mark.parametrize('num', [-2, 0])
def test_error(num):
    with pytest.raises(ValueError):
        nth_fibonacci(num)

if __name__ == '__main__':
    pytest.main()
