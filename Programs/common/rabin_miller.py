# Проверка на простоту тестом Миллера-Рабина
import random

from fast_pow import power as pw

# Проверка на вероятную простоту.
def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # Представляем n-1 в виде (2^r) * d
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    # Повторяем тест k раз
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pw(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pw(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Запуск демо-режима этого модуля
if __name__ == "__main__":
    print("Введите 2 числа через пробел: n, k. Будет дан ответ, составное ли n или вероятно простое.")
    n, k = map(int, input().split())
    if (miller_rabin(n, k)):
        print(f"Вероятно {n} простое")
    else:
        print(f"Число {n} составноe")

# Примеры ввода-вывода программы
# python3 rabin_miller.py
# Введите 2 числа через пробел: n, k. Будет дан ответ, составное ли n или вероятно простое.
# 997 3
# Вероятно 997 простое
#
# python3 rabin_miller.py
# Введите 2 числа через пробел: n, k. Будет дан ответ, составное ли n или вероятно простое.
# 1025 2
# Число 1025 составноe 
