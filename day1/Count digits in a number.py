# Count digits in a number

# Taking input from the user and converting it to an integer
num = int(input("Enter a number: "))

# Initializing a variable to count the digits
digit_count = 0

# Using a while loop to count the digits in the number
while num > 0:
    # Removing the last digit from the number
    num = num // 10
    
    # Incrementing the digit count
    digit_count += 1

# Displaying the digit count
print("The number of digits in the entered number is:", digit_count)