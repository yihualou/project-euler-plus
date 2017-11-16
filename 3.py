from math import sqrt

prime_limit = 100000
primes = set(range(2, prime_limit + 1))
for i in range(2, int(sqrt(prime_limit)) + 1):
  if i in primes:
    j = i * i
    while (j <= prime_limit):
      primes.discard(j)
      j += i


def is_prime(v):
  if v in primes:
    return True

  for i in range(2, int(sqrt(v))):
    if v % i == 0:
      return False

  primes.add(v)
  return True


t = int(input())
for i in range(t):
  n = int(input())
  maxf = 0
  for j in range(2, int(sqrt(n)) + 1):
    if not is_prime(j):
      continue

    if n % j == 0:
      while n % j == 0:
        n //= j

      maxf = j

  if n > 1:
    maxf = n

  print(maxf)
