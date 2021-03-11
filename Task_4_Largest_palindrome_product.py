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


def find_palindrome(n):
    num = n

    while num > 0:
        res = num * n
        if res == reverse_number(res):
            return res
        num -= 1


if __name__ == '__main__':
    print(f'Palindrome of two 3-digit number: {find_palindrome(999)}')

    assert find_palindrome(123) == 10701
    assert find_palindrome(99) == 9009
    assert find_palindrome(999) == 90909
