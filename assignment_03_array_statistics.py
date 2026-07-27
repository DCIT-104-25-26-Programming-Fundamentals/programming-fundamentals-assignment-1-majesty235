# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def calculate_sum(numbers):
    """Returns the sum of all numbers in the list (no built-in sum())."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Returns the average of all numbers in the list."""
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    """Returns the largest number in the list (no built-in max())."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def find_minimum(numbers):
    """Returns the smallest number in the list (no built-in min())."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: The number of values must be a positive integer.")
        return

    numbers = []
    for i in range(n):
        value = float(input(f"Enter number {i + 1}: "))
        numbers.append(value)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)

    print("\nResults:")
    print(f"Sum:     {total:g}")
    print(f"Average: {average:g}")
    print(f"Maximum: {maximum:g}")
    print(f"Minimum: {minimum:g}")


if __name__ == "__main__":
    main()