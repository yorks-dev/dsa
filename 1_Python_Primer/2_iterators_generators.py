# ITERATORS

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

import cmath  # To handle complex numbers if needed

# Define an iterator
iter1 = iter(list1)  # Example iterator

try:
    while True:
        a = cmath.sqrt(-1)  # Use cmath for complex numbers
        print(next(iter1), end=" ")  # Access the next element
except Exception as e:
    print("Done -", repr(e))  # Always use repr


# GENERATORS
