# Amstrong Number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

# Taking input from the user and converting it to an integer
num = int(input("Enter a number: "))

# Counting the digits in the number
digit_count = 0
temp = num
while temp > 0:
    temp = temp // 10
    digit_count += 1

# Calculating the sum of digits raised to the power of the number of digits
digit_sum = 0
temp = num
while temp > 0:
    last_digit = temp % 10
    digit_sum += last_digit ** digit_count
    temp = temp // 10

# Checking if the number is an Armstrong number
if digit_sum == num:
    print("The entered number is an Armstrong number.")
else:
    print("The entered number is not an Armstrong number.")
