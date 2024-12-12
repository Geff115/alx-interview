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

    # Finding the maximum value of the array
    max_value = max(nums)

    # Precomputing prime using a helper function
    primes, prime_count = compute_primes(max_value)

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

        # Determining the winner for the round using a helper function
        winner = simulate_round(n, prime_count)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    # Determining the overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None


def compute_primes(limit):
    """
    Computes prime numbers and their cumulative count up to a given limit.

    Args:
        limit (int): The upper bound for prime calculation.

    Returns:
        tuple: A boolean list indicating primes and a
        list of cumulative prime counts.
    """
    prime = [True for _ in range(limit + 1)]
    prime[0] = prime[1] = False  # 0 and 1 are not prime
    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False

    prime_count = [0] * (limit + 1)
    for i in range(1, limit + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime[i] else 0)

    return prime, prime_count


def simulate_round(n, prime_count):
    """
    Simulates a single round of the prime game.

    Args:
        n (int): The upper bound of the current round.
        prime_count (list): Precomputed cumulative prime counts.

    Returns:
        str: The winner of the round ("Maria" or "Ben").
    """
    primes_left = prime_count[n]
    turn = 0  # 0 for Maria, 1 for Ben

    while primes_left > 0:
        primes_left -= 1
        turn = 1 - turn  # Alternate turns

    return "Ben" if turn == 0 else "Maria"
