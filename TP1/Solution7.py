# Without converting numbers to strings, write three functions that work digit by digit with a while loop: 
# • digit_sum(n) adds up the digits: 2026 → 2 + 0 + 2 + 6 = 10. 
# • reverse_number(n) reverses the digits: 2026 → 6202. 
# • is_palindrome(n) returns True when a number reads the same in both directions (12321). 
# (a) Test the three functions with 2026, 12321 and 9875. 
# (b) Count how many palindromes there are from 10 to 999.


def digit_sum(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10

    return total


def reverse_number(n):
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return reversed_num


def is_palindrome(n):
    if n < 0:
        return False

    return n == reverse_number(n)

count = 0
n = 10

while n <= 999:
    if is_palindrome(n):
        count += 1

    n += 1

# Test the three functions
numbers = [2026, 12321, 9875, 12345654321, 1212, 102201]

for n in numbers:
    print("Number:", n)
    print("Digit sum:", digit_sum(n))
    print("Reversed:", reverse_number(n))
    print("Palindrome:", is_palindrome(n))
    print("Number of palindromes:", count)
    print()


