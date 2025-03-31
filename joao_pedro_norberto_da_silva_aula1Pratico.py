import random
import time

random_vector = [random.randint(1, 1000000) for i in range(100000)]

def is_prime_recursive(n: int, divisor: int = 2) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True

    return is_prime_recursive(n, divisor + 1 if divisor == 2 else divisor + 2)


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

start = time.time()
result_list_recursive = [is_prime_recursive(n) for n in random_vector]
end = time.time()
print(f"Tempo (recursivo): {end - start:.6f} segundos")

start = time.time()
result_list_iterative = [is_prime_number(n) for n in random_vector]
end = time.time()
print(f"Tempo (iterativo): {end - start:.6f} segundos")
