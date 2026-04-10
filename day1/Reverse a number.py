# Reverse a number

# Taking input from the user and converting it to an integer
num = int(input("Enter a number: "))

# Initializing a variable to store the reversed number
reversed_num = 0

# Using a while loop to reverse the number
while num > 0:

    # Getting the last digit of the number
    last_digit = num % 10
    
    # Adding the last digit to the reversed number
    reversed_num = (reversed_num * 10) + last_digit
    
    # Removing the last digit from the original number
    num = num // 10

# Displaying the reversed number
print("The reversed number is:", reversed_num)