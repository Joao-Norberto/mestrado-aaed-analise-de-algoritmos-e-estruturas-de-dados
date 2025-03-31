import random

random_vector = [random.randint(1, 1000000) for _ in range(100000)]

def is_prime_number(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

result_list = [is_prime_number(n) for n in random_vector]

