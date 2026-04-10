# Largest of 2 numbers

# Taking input from the user and converting it to a float
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Finding the largest number using an if-else statement
if num1 > num2:
    largest = num1
else:
    largest = num2

# Displaying the largest number
print("The largest number between", num1, "and", num2, "is:", largest)