# Sum of first N numbers

# Taking input from the user and converting it to an integer
n = int(input("Enter a positive integer: "))

# Initializing the sum variable
total_sum = 0

# Using a for loop to calculate the sum of the first N numbers
for i in range(1, n + 1):
    total_sum += i

# Displaying the result
print("The sum of the first", n, "numbers is:", total_sum)