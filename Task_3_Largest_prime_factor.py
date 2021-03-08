"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def find_max_divider(n):
    d = 2
    last_d = 0
    while n > 1:
        if n % d == 0:
            n = n / d
            last_d = d
            d = 2
            continue
        d += 1

    return last_d


if __name__ == '__main__':
    print(find_max_divider(600851475143))
