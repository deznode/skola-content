#!/usr/bin/env python3
"""
Introduction to Python - Complete Solution
Skola.dev Tutorial
"""


def greet(name: str) -> str:
    """Return a personalized greeting."""
    return f"Bondia, {name}! Bem-vindu a Python!"


def calculate_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle."""
    return width * height


def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0


def count_vowels(text: str) -> int:
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def fizzbuzz(n: int) -> list[str]:
    """Generate FizzBuzz sequence up to n."""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def main():
    # Variables and types
    name = "Maria"
    age = 25
    height = 1.65
    is_student = True

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}m")
    print(f"Is student: {is_student}")
    print()

    # Using our functions
    print(greet(name))
    print(f"Area of 5x3 rectangle: {calculate_area(5, 3)}")
    print(f"Is 42 even? {is_even(42)}")
    print(f"Vowels in 'Hello World': {count_vowels('Hello World')}")
    print()

    # FizzBuzz demonstration
    print("FizzBuzz (1-15):")
    print(", ".join(fizzbuzz(15)))


if __name__ == "__main__":
    main()
