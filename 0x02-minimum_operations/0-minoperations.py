#!/usr/bin/python3
"""
This script contains a function that calculates the fewest
number of operations needed to result in exactly n H chracters
in the file.
"""


def minOperations(n):
    """
    ARGS:
        - n: an integer

    RETURN:
        - The minimum number of operations needed to result in
        exactly n H chracters in the file
    """
    if n <= 1:
        return 0  # Return 0 if n is impossible or no operations are needed

    counter = 0
    smallest_prime_factor = 2

    while n > 1:
        # while n is divisible by the smallest prime factor
        while n % smallest_prime_factor == 0:
            # Adding the prime factors value to the counter
            counter += smallest_prime_factor
            # floor division of n to move forward with factorization
            n //= smallest_prime_factor

        # Moving to the next factor if 2 isn't a prime factor of n
        smallest_prime_factor += 1

    return counter
