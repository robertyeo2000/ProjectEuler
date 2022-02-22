
# Primes
def nthPrime(n):
    primeList = [2]
    primeAttempt = 3
    while len(primeList) < n:
        if __isPrime(primeAttempt, primeList):
            primeList.append(primeAttempt)
        primeAttempt += 1
    return primeList[-1]


def allPrimesBelow(n):
    allNumbers = set(range(n, 1, -1))
    primes = []
    while len(allNumbers) > 0:
        p = allNumbers.pop()
        primes.append(p)
        allNumbers.difference_update(set(range(p*2, n+1, p)))
    return primes


def __isPrime(n, primeList):
    for prime in primeList:
        if n % prime == 0:
            return False
    return True


def numberOfDivisors(n):
    numDivisors = 0
    for divisorAttempt in range(1, int(n**.5)+1):
        if n % divisorAttempt == 0:
            numDivisors += 2
    if n**.5 == int(n**.5):
        numDivisors += 1
    return numDivisors
