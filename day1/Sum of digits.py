# Sum of digits of a number

# Taking input from the user and converting it to an integer
num = int(input("Enter a number: "))

# Initializing a variable to store the sum of digits
digit_sum = 0

# Using a while loop to calculate the sum of digits
while num > 0:
    # Getting the last digit of the number
    last_digit = num % 10
    
    # Adding the last digit to the sum
    digit_sum += last_digit
    
    # Removing the last digit from the original number
    num = num // 10

# Displaying the sum of digits
print("The sum of the digits is:", digit_sum)
