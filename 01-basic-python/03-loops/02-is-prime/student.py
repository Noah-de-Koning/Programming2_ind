# Write your code here
def is_prime (n):
    for k in range (2, n):
        if n % k is 0:
            return False
    return n > 1