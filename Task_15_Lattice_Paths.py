"""
Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly  routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

"""

from math import comb

if __name__ == "__main__":
    k, n = (20, 20)
    result = comb(k + n, n)
    print(result)
