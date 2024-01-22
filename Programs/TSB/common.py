import sys
sys.path.append('../common/')

from gen_prime import gen_prime_with_fix_len
from rabin_miller import miller_rabin as check_simple

# Процедура для генерации простого числа  по его остатку от ключа злоумышленника.
# Используется как в генерации, так и злоумышленником.
def gen(x_small, A, t):
    k = gen_prime_with_fix_len(t // 4, x_small)
    X = None
    while X is None:
        if check_simple(A * k + x_small, t * 10):
            X = A * k + x_small
        else:
            k = k + 1
    return X