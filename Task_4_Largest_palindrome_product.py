"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def reverse_number(n, partial=0):
    if n == 0:
        return partial
    return reverse_number(n // 10, partial * 10 + n % 10)


def find_palindrome():
    for x in range(999, 900, -1):
        for y in range(x, 900, -1):
            num = x * y
            if reverse_number(num) == num:
                return num


if __name__ == '__main__':
    print(f'Largest palindrome of two 3-digit numbers: {find_palindrome()}')
