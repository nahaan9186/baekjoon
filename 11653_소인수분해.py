import math

n = int(input())
res = []

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes_up_to(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(limit + 1) if is_prime[p]]

limit = int(math.sqrt(n)) + 1
primes = generate_primes_up_to(limit)
k = 0

while True:
    if n == 1:
        break
    if k < len(primes) and n % primes[k] == 0:
        res.append(primes[k])
        n //= primes[k]
    elif k < len(primes):
        k += 1
    else:
        if is_prime(n):
            res.append(n)
            break
        else:
            k += 1
            while not is_prime(k):
                k += 1
            res.append(k)
            n //= k

for factor in res:
    print(factor)
