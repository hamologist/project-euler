import fileinput
from math import sqrt
from typing import List


def prime_factorization(lim: int) -> List[int]:
    primes: List[int] = []

    while lim % 2 == 0:
        primes.append(2)

        lim = int(lim / 2)

    for i in range(3, int(sqrt(lim)), 2):
        while lim % i == 0:
            primes.append(i)

            lim = int(lim / i)

    if lim > 2:
        primes.append(lim)

    return primes

if __name__ == '__main__':
    user_input: List[str] = [line.strip().split(' ') for line in fileinput.input()][0]
    limit = int(user_input[0])
    factors = prime_factorization(limit)

    print(factors)
    factors = sorted(list(set(factors)))
    print(factors)
    if len(factors) > 0:
        print(factors[-1])
