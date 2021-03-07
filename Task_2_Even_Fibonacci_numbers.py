"""
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b + a


def fib_even():
    for i in fib():
        if i % 2 == 0:
            yield i


def sum_even():
    sum_elements = 0
    for i in fib_even():
        if i > 4000000:
            break
        sum_elements += i

    return sum_elements


if __name__ == '__main__':
    print(sum_even())