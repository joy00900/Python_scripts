# Create a set with duplicate elements
my_set = {1, 2, 3, 4, 5, 5, 5}

# Add element 4 to the set
my_set.add(4)

# Check if 5 is in the set
print(5 in my_set)  # Output: True

# Print the set (duplicates have been removed)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Create sets from strings
a = set('abracadabra')
b = set('alacazam')

# Print the unique letters in sets a and b
print(a)  # Output: {'a', 'r', 'b', 'c', 'd'}
print(b)  # Output: {'a', 'l', 'c', 'z', 'm'}

# Set operations
print(a - b)  # Output: {'d', 'b', 'r'} (letters in a but not in b)
print(a | b)  # Output: {'a', 'c', 'b', 'l', 'd', 'z', 'r', 'm'} (letters in a or b or both)
print(a & b)  # Output: {'a', 'c'} (letters in both a and b)
print(a ^ b)  # Output: {'b', 'l', 'd', 'z', 'r', 'm'} (letters in a or b but not both)

