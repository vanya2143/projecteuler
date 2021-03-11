"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

NUMBER = 20


def total_number():
    """
    The function looks for the total number that is divisible by all numbers from 1 to 20
    """
    mul = NUMBER
    number = mul

    while mul > 0:
        if number % mul != 0:
            number *= mul
            mul -= 1
            continue

        mul -= 1
    return number


def check(n):
    """
    The function checks is a number divisible by numbers from 1 to NUMBER
    :param n: number
    :return Bool
    """
    count = 0
    for i in range(1, NUMBER + 1):
        if n % i == 0:
            count += 1

    return True if count == NUMBER else False


def smallest_total_number():
    """
    The function finds smallest total number that
    is evenly divisible by all of the numbers
    from 1 to NUMBER
    """

    total = total_number()
    smallest_number = 0
    current_number = total

    while check(current_number):
        if current_number % 2 == 0:
            smallest_number = current_number
            current_number = current_number // 2

    return smallest_number


if __name__ == '__main__':
    print(smallest_total_number())

    assert smallest_total_number() == 232792560

    NUMBER = 10
    assert smallest_total_number() == 2520
