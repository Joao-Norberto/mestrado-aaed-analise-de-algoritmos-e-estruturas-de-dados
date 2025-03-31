import random

random_vector = [random.randint(1, 1000000) for i in range(100000)]

def is_prime_number(n: int):
    if n <= 1:
        return False
    
    for i in range(2, n//2):
        if n % i == 0:# se o resto da divisão for 0, a divisão é exata e o número não é primo
            return False

    return True

