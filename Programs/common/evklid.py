# Вычисление обратного к числу a по модулю mod

def calc_inverse(a, mod):
    def euclidean_algorithm(a, b):
        if b == 0:
            return a, 1, 0
        else:
            gcd, x, y = euclidean_algorithm(b, a % b)
            return gcd, y, x - (a // b) * y
      
    gcd, x, _ = euclidean_algorithm(a, mod)
    if gcd != 1:
        raise ValueError("Обратный элемент не существует")
    else:
        return x % mod

# Запуск демо-режима этого модуля
if __name__ == "__main__":
    print("Введите 2 числа через пробел: a, mod. a - для какого числа вычисляем обратное. mod - по какому модулю.")
    a, mod = map(int, input().split())
    obr = calc_inverse(a, mod)
    print(f"obr = {obr}. {a} * {obr} = {a * obr}. {a * obr} % {mod} = {a * obr % mod}")

# Примеры ввода-вывода программ
# python3 evklid.py
# Введите 2 числа через пробел: a, mod. a - для какого числа вычисляем обратное. mod - по какому модулю.
# 17 31
# obr = 11. 17 * 11 = 187. 187 % 31 = 1
#
#python3 evklid.py
#Введите 2 числа через пробел: a, mod. a - для какого числа вычисляем обратное. mod - по какому модулю.
#2434234217 9182321318231291321213531
#obr = 4339706997783298193925513. 2434234217 * 4339706997783298193925513 = 10563863265758447614767785293878321. 10563863265758447614767785293878321 % 9182321318231291321213531 = 1
