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

#Test 4
def test_non_integer_input():
    with pytest.raises(ValueError):
        Fibonacci("ten")

#Test 5
def test_negative_input():
    with pytest.raises(ValueError):
        Fibonacci(-5)

#Test 6
def test_is_iterable():
    fib = Fibonacci(5)
    assert iter(fib) is fib

#Test 7
def test_stop_iteration():
    fib = Fibonacci(2)
    next(fib)
    next(fib)
    with pytest.raises(StopIteration):
        next(fib)