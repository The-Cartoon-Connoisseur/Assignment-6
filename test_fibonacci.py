import pytest
from fibonacci import Fibonacci

#Test 1
def test_fibonacci_sequence():
    fib = Fibonacci(6)
    assert list(fib) == [0, 1, 1, 2, 3, 5]

#Test 2
def test_zero_terms():
    fib = Fibonacci(0)
    assert list(fib) == []

#Test 3
def test_one_term():
    fib = Fibonacci(1)
    assert list(fib) == [0]