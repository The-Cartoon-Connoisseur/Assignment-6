import pytest
from fibonacci import Fibonacci

#Test 1
def test_fibonacci_sequence():
    fib = Fibonacci(6)
    assert list(fib) == [0, 1, 1, 2, 3, 5]