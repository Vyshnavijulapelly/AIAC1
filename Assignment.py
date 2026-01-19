#Question 1:generate a python program that checks whether a given number is a palindrome
def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]
print(is_palindrome(121))  
print(is_palindrome(123))
# #QUESTION 2 : write a python program that compute factorial of a number 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
# #QUESTION 3 : write a python program that checks given number is an armstrong or not 
# #output should be like Armstrong number or Not an Armstrong number
def is_armstrong(num):
    str_num = str(num)
    num_digits = len(str_num)
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
    if sum_of_powers == num:
        return "Armstrong number"
    else:
        return "Not an Armstrong number"
print(is_armstrong(153))
print(is_armstrong(370))
print(is_armstrong(123))
#QUESTION 4 : to generate an optimized Python program that classifies a number as prime, composite, or neither
def classify_number(num):
    if num <= 1:
        return "Neither prime nor composite"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Composite"
    return "Prime"  
print(classify_number(11))
print(classify_number(15))
print(classify_number(1))
#QUESTION 5 : generate a Python function that checks whether a given number is a perfect number
def is_perfect_number(num):
    if num < 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num
print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(12))
print(is_perfect_number(14))
#Question 6 : generate a Python program that determines whether a given number is even or odd, including proper input validation
#output should be like Even or Odd
def is_even_or_odd(num):
    if not isinstance(num, int):
        return "Invalid input. Please enter an integer."
    return "Even" if num % 2 == 0 else "Odd"
print(is_even_or_odd(8))
print(is_even_or_odd(15))
print(is_even_or_odd(0))