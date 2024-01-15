# Генерация простого числа заданной длины с возможностью указать сид генерации

import random

from rabin_miller import miller_rabin as check_simple

def gen_prime_with_fix_len(byte_length, seed = None):
    assert (byte_length >= 2)
    if seed is not None:
        random.seed(seed)
    while True:
        A = random.randint(2 ** (byte_length - 1), 2 ** byte_length)
        # Если собираемся проверять число A на простоту, число итераций советують брать равным log_2(A)
        # Число t искомое число итераций
        if check_simple(A, byte_length):
            return A
        # Есть оценка числа простых меньших N. Их будет N / log_e(N).
        # Cоответственно за log_e(N) < log_2(N) = t итераций число A окажется простым.

# Запуск демо-режима этого модуля
if __name__ == "__main__":
    print("Введите 1 или 2 числа. len или len seed. len - длина результата в байтах. seed - ключ генерации псевдослучайных чисел.")
    print("Для одинаковых пар {len, seed} результат будет одинаковый.")
    inp = input().split()
    seed = None
    if len(inp) == 1:
        length = int(inp[0])
    elif len(inp) == 2:
        length = int(inp[0])
        seed = int(inp[1])
    else:
        print(f"Wrong numbers count. Expected 1 or 2, got {len(inp)}: {inp}")
        assert 1 <= len(inp) and len(inp) <= 2
    res = gen_prime_with_fix_len(length, seed)
    print(bin(res))

# Примеры ввода-вывода программы
# python3 gen_prime.py
# Введите 1 или 2 числа. len или len seed. len - длина результата в байтах. seed - ключ генерации псевдослучайных чисел.
# Для одинаковых пар {len, seed} результат будет одинаковый.
# 10
# 0b1101011001
#
# python3 gen_prime.py
# Введите 1 или 2 числа. len или len seed. len - длина результата в байтах. seed - ключ генерации псевдослучайных чисел.
# Для одинаковых пар {len, seed} результат будет одинаковый.
# 10
# 0b1111000111
#
# python3 gen_prime.py
# Введите 1 или 2 числа. len или len seed. len - длина результата в байтах. seed - ключ генерации псевдослучайных чисел.
# Для одинаковых пар {len, seed} результат будет одинаковый.
# 20 15
# 0b11011011000100011011
#
# python3 gen_prime.py
# Введите 1 или 2 числа. len или len seed. len - длина результата в байтах. seed - ключ генерации псевдослучайных чисел.
# Для одинаковых пар {len, seed} результат будет одинаковый.
# 20 15
# 0b1101101100010001101

