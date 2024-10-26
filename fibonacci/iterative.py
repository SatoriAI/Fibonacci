def fibonacci(n: int) -> int:
    if n < 2:
        return n

    a = 0
    b = 1

    for i in range(2, n+1):
        temporary = a + b
        a = b
        b = temporary
        print(f"fibonacci({i}) = {b}")

    return b


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
