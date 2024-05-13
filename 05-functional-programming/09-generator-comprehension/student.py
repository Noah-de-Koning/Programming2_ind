from itertools import count

def is_prime(n):
    return n >= 2 and all(n % _ != 0 for _ in range(2, n))
                

def primes():
    return (x for x in count(2) if is_prime(x))