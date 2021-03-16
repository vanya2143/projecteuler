"""


The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_square_difference():
    sum_of_the_squares = sum([x ** 2 for x in range(101)])
    square_of_the_sum = sum([x for x in range(101)]) ** 2
    return square_of_the_sum - sum_of_the_squares


if __name__ == '__main__':
    print(sum_square_difference())
