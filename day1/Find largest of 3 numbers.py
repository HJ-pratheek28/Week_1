# Largest of 3 numbers

# Taking input from the user and converting it to a float
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding the largest number using nested if-else statements
if num1 > num2:
    if num1 > num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 > num3:
        largest = num2
    else:
        largest = num3

# Displaying the largest number
print("The largest number between", num1, "and", num2, "and", num3, "is:", largest)