"""
Write a function fib() that a takes an integer n and returns the nth fibonacci
number.
Let's say our fibonacci series is 0-indexed and starts with 0. So:

    fib(0) # => 0
    fib(1) # => 1
    fib(2) # => 1
    fib(3) # => 2
    fib(4) # => 3
    ...
"""
import common


@common.print_return
def fib(n):
    if n == 0:
        return 0

    curr_fibo_num = prev_fibo_num = 1
    while n > 2:
        curr_fibo_num, prev_fibo_num = curr_fibo_num + prev_fibo_num, curr_fibo_num
        n = n - 1
    return curr_fibo_num

if __name__ == '__main__':
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
