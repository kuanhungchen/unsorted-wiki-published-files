from typing import List


"""Returns all prime numbers that is smaller or equal to n."""
def findPrimeNumbers(n: int) -> List[int]:
    primes = []
    visited = [False for _ in range(n + 1)]
    for i in range(2, n + 1):
        if not visited[i]:
            primes.append(i)
        for prime in primes:
            if i * prime > n:
                break
            visited[i * prime] = True
            if i % prime == 0:
                break
    return primes
