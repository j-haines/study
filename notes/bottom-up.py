"""
### Bottom-Up Algorithms
    - a way to avoid recursion (top-down)
        - saves memory cost of recursive functions building call stack
    - starts from the beginning vs starting at the end and working backwards

## e.g.
# Top-Down
```
def product_1_to_n(n):
    return n * product_1_to_n(n - 1) if n > 1 else 1
```

# Bottom-up
```
def product_1_to_n(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result
```

    - coin_recursive.py starts with final value of amount and breaks it down
        into subproblems with smaller values
    - coin.py computes small values first, using those to iteratively compute
        the answer for higher values
"""
