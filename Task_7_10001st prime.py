"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import sqrt


def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def find_prime_number():
    digit = 0
    limit = 10001
    index = 2
    p_index = 0

    while p_index < limit:
        if is_prime(index):
            digit = index
            p_index += 1
        index += 1

    return digit


if __name__ == '__main__':
    print(find_prime_number())
