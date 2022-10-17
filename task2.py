# A twin of a word is a word written with the same letters (case insensitive) but not necessarily in the same order.
# For example Silent is a twin of Listen.
# The is_twin(a, b) function should return True if b is the twin of a and False otherwise
# a and b are two strings and are not None.
# Write the body of the is_twin(a, b) function.

a = input(str("Please enter a word"))
b = input(str("Please enter another word"))

def is_twin(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

print(is_twin(a, b))


