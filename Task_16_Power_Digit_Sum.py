"""
2^15 = 32786 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
What is the sum of the digits of the number 2^1000?
"""
from functools import cache


@cache
def get_sum(n):
    if n // 10 == 0:
        return n

    return n % 10 + get_sum(n // 10)


if __name__ == "__main__":
    assert get_sum(2**15) == 26
    print(get_sum(2 ** 1000))
