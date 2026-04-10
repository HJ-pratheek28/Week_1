# Swap without temp variable

# Taking input from the user
a = input("Enter the first value: ")
b = input("Enter the second value: ")

# Swapping the values without using a temporary variable
a, b = b, a
# Displaying the swapped values
print("After swapping:")
print("First value:", a)
print("Second value:", b)
