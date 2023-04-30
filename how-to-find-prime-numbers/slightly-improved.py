from typing import List


"""Returns all prime numbers that is smaller or equal to n."""
def findPrimeNumbers(n: int) -> List[int]:
    primes = []
    for candidate in range(2, n + 1):
        sqrt = int(pow(candidate, 0.5))
        for factor in range(2, sqrt + 1):
            if candidate % factor == 0:
                # Not a prime.
                break
        else:
            primes.append(candidate)
    return primes
