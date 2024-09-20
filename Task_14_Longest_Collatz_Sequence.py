"""
The following iterative sequence is defined for the set of positive integers:

If n is even, then n → n/2
If n is odd, then n → 3n + 1
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers eventually reach 1.

Question: Which starting number, under one million, produces the longest chain?

Note: Once the chain starts, the terms are allowed to go above one million.
"""


def get_sequence_length(digit):
    if digit == 1:
        return 1

    if digit % 2 == 0:
        return 1 + get_sequence_length(int(digit / 2))
    elif digit % 2 != 0:
        return 1 + get_sequence_length(digit * 3 + 1)


if __name__ == "__main__":
    max_starting_number = 0
    max_length = 0
    for i in range(1, 1000000):
        res = get_sequence_length(i)
        if res > max_length:
            max_starting_number = i
            max_length = res

    print(max_starting_number)

# the answer is 837799
