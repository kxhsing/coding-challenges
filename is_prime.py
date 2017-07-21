import math
def is_prime(num):
    prime = True
    limit = int(math.sqrt(num))+1
    for i in range(2, limit):
        if num % i == 0:
            prime = False

    return prime
