# find_largest(numbers) should return the largest number from numbers.
# The array numbers always contains at least one number.
# Implement find_largest(numbers).

numbers = [5, 7, 3, 1, 2]

def find_largest(numbers):
    max = numbers[0]

    for x in numbers:
        if x > max:
            max = x

    return max
print(f"{find_largest(numbers)} is the biggest number in the list")