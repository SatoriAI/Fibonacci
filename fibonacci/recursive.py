def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n=n-1) + fibonacci(n=n-2)


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
