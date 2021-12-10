from typing import Iterator

def fibonacci(n: int) -> Iterator[int]:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

if __name__ == "__main__":
    for element in fibonacci(20):
        print(element)
