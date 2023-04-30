from typing import List


"""Returns all prime numbers that is smaller or equal to n."""
def findPrimeNumbers(n: int) -> List[int]:
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False
    i = 2
    while i * i <= n:
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
        i += 1
    primes = [p for (p, flag) in enumerate(is_prime) if flag]
    return primes
