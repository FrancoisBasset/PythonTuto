"""Fibonacci numbers module."""

import sys

def fib(n: int):
    """Print the Fibonacci numbers"""
    a, b = 0, 1

    while a < n:
        print(a, end=" ")
        a, b = b, a + b

    print()

def fib2(n: int) -> list:
    """Return the Fibonacci numbers"""
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)
        a, b = b, a + b

    return result

if __name__ == "__main__":
    try:
        number = int(sys.argv[1])
        fib(number)
    except IndexError:
        print("No argument")
    except ValueError:
        print("Bad argument type")
