# Быстрое возведение в степень по модулю
def power(x, y, p):
    assert p >= 0
    result = 1
    x %= p
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % p
        y //= 2
        x = (x * x) % p
    return result

# Запуск демо-режима этого модуля
if __name__ == "__main__":
    print("Введите 3 числа через пробел: x, y, p. Значение функции будет равно (x ^ y) % p.")
    x, y, p = map(int, input().split())
    print(f"({x} ^ {y}) % {p} = {power(x, y, p)}")

# Примеры ввода-вывода программы
# python3 fast_pow.py
# Введите 3 числа через пробел: x, y, p. Значение функции будет равно (x ^ y) % p.
# 2 10 1000
# (2 ^ 10) % 1000 = 24
