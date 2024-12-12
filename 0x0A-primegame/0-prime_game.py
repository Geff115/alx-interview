#!/usr/bin/python3
"""
Solving the prime game problem by using
Sieve of Eratosthenes algorithm
"""


def isWinner(x, nums):
    """
    ARGS:
        - x: number of rounds.
        - numbs: an array of n

    n and x will not be larger than 10,000

    RETURN: name of the player that won the most rounds
    """
    if not x or not nums:
        return None

    if not isinstance(nums, list):
        return None

    # Finding the maximum value of the array
    nums_length = len(nums)
    max_value = nums[0]
    for i in range(1, nums_length):
        if nums[i] > max_value:
            max_value = nums[i]

    # Creating a list of Boolean values
    prime = [True for i in range(max_value + 1)]
    # Explicitly initializing prime[0] and prime[1] to false
    # Since 0 and 1 are not prime numbers
    prime[0] = prime[1] = False
    p = 2
    while (p * p <= max_value):
        if prime[p]:
            # Mark multiples of p as False
            for i in range(p * p, max_value + 1, p):
                prime[i] = False
        p += 1

    # Precomputing prime counts
    prime_count = [0] * (max_value + 1)
    for i in range(1, max_value + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime[i] else 0)

    # Game logic
    # Initializing counters for wins
    maria_wins = 0
    ben_wins = 0

    # Simulating each round
    for n in nums:
        # Handling edge case where no primes are available
        if n == 1:
            ben_wins += 1
            continue

        primes_left = prime_count[n]
        turn = 0  # Maria starts firs (turn = 0), Ben is second (turn = 1)

        while primes_left > 0:
            # Reduce primes_left by 1 (one prime and its multiples are removed)
            primes_left -= 1
            turn = 1 - turn  # Alternate turns

        # Determining the winner of the round
        if turn == 1:
            # Maria's turn ends the game, Ben wins
            ben_wins += 1
        else:
            # Ben's turn ends the game, Maria wins
            maria_wins += 1

    # Determining the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
