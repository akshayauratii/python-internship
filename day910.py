# Program to input two numbers and print their sum
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
total_sum = first_number + second_number
print(f"The sum of {first_number} and {second_number} is: {total_sum}")


# Program to calculate the area of a rectangle
rectangle_length = float(input("Enter the length of the rectangle: "))
rectangle_width = float(input("Enter the width of the rectangle: "))
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {rectangle_area}")


# Program to calculate simple interest
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the annual rate of interest (in %): "))
time_period_years = float(input("Enter the time period (in years): "))
calculated_simple_interest = (principal_amount * rate_of_interest * time_period_years) / 100
print(f"The calculated Simple Interest is: {calculated_simple_interest}")


# Program to convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")


# Program to calculate HRA and DA from basic salary
basic_salary = float(input("Enter employee basic salary: "))
hra = 0.20 * basic_salary
da = 0.10 * basic_salary
print(f"Basic Salary: {basic_salary}")
print(f"HRA (20%): {hra}")
print(f"DA (10%): {da}")
print(f"Total Salary: {basic_salary + hra + da}")


# Program to check if a number is positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Program to find the largest among two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"The largest number is {num1}")
elif num2 > num1:
    print(f"The largest number is {num2}")
else:
    print("Both numbers are equal.")


# Program to check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


# Program to check whether a year is a leap year or not
year = int(input("Enter a year: "))
if (year % 400 == 0):
    print(f"{year} is a leap year.")
elif (year % 100 == 0):
    print(f"{year} is not a leap year.")
elif (year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Program to print numbers from 1 to 100
for i in range(1, 101):
    print(i)


# Program to find sum of first N natural numbers
N = int(input("Enter a positive integer N: "))
sum_formula = N * (N + 1) // 2
print(f"Sum of first {N} natural numbers (formula method): {sum_formula}")
sum_loop = 0
for i in range(1, N + 1):
    sum_loop += i
print(f"Sum of first {N} natural numbers (loop method): {sum_loop}")


# Program to print multiplication table of a given number
num = int(input("Enter a number: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# Program to calculate factorial of a number
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")


# Function to find square of a number
def square(num):
    return num * num

n = int(input("Enter a number: "))
print(f"The square of {n} is {square(n)}")


# Function to find maximum of two numbers
def maximum(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The maximum of {num1} and {num2} is {maximum(num1, num2)}")


# Function to check whether a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."

n = int(input("Enter a number: "))
print(check_even_odd(n))


# Program to create a list of 10 numbers and print all elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The list of numbers is:")
for num in numbers:
    print(num)


# Program to find the largest element in a list
numbers = [12, 45, 67, 23, 89, 34, 76, 90, 11, 54]
largest = max(numbers)
print(f"The largest element in the list is: {largest}")
largest_loop = numbers[0]
for num in numbers:
    if num > largest_loop:
        largest_loop = num
print(f"(Loop method) The largest element in the list is: {largest_loop}")


# Program to count even numbers in a list
numbers = [10, 15, 22, 33, 40, 55, 60]
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("List:", numbers)
print("Number of even elements:", even_count)


# Reverse a number
num = int(input("Enter a number: "))
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print(f"Reversed number: {rev}")


# Check if a number is palindrome
num = int(input("Enter a number: "))
rev = str(num)[::-1]
if str(num) == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# Count digits in a number
num = int(input("Enter a number: "))
count = len(str(num))
print(f"Number of digits: {count}")


# Find sum of digits
num = int(input("Enter a number: "))
sum_digits = 0
temp = num
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print(f"Sum of digits: {sum_digits}")


# Generate Fibonacci series up to N terms
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Check if a number is prime
num = int(input("Enter a number: "))
is_prime = True
if num < 2:



