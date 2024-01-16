import sys
sys.path.append('../common/')

from common import gen
from evklid import calc_inverse
from gen_prime import gen_prime_with_fix_len
from rabin_miller import miller_rabin as check_simple
from file_funcs import write_line_to_file

# Генерируем ключ злоумышленника
def gen_secret_key(t, c):
    len_T = t - c
    T = gen_prime_with_fix_len(len_T)
    return T

# Процедура, вычисляющая открытый и закрытый ключи RSA.
def gen_keys(t, c, T, K):
    len_rq = t - c
    abort_flag = False
    while not abort_flag:
        q = gen_prime_with_fix_len(len_rq)
        r = gen_prime_with_fix_len(len_rq)
        k = 2
        while k <= K:
            p = r + (k * q - r) % T
            if check_simple(p, len_rq * 10):
                abort_flag = True
                break
            k = k + 1
    n = p * q
    fi_n = (p - 1) * (q - 1)
    # Не предполагается работа с такими маленькими числами.
    # Если fi_n не более 4 бит, то p_small - 1битное число, а раз простое, то хотя бы 2.
    assert fi_n > 17
    e = 17
    d = calc_inverse(e, fi_n)
    return e, d, n

# Интерфейс пользователя. Интерактивная генерация ключей.
def demo_key_generation():
    print("Введите 1 число t - число бит в числах p и q. Обычно используют 256, 512, 1024, 2048, 4096")
    t = int(input())
    c = 7
    T = gen_secret_key(t, c)
    K = (t - c)
    print(f"Секретный ключ злоумышленника {bin(T)} {bin(K)}")
    write_line_to_file(bin(T) + " " + bin(K), "backdoor_key.txt")
    e, d, n = gen_keys(t, c, T, K)
    print(f"Открытый ключ ({e}, {n})")
    print(f"Закрытый ключ ({d}, {n})")
    write_line_to_file(bin(e) + " " + bin(n), "public_key.txt")
    write_line_to_file(bin(d) + " " + bin(n), "private_key.txt")

# Интерфейс пользователя. Инструкция по использованию.
def print_how_to_start_and_exit(exit_code = 1):
        print("Select Programs/sandbox directory")
        print("Usage python3 ../SSB/generation.py --help")
        print("Usage python3 ../SSB/generation.py")
        exit(exit_code)

# Запуск демо-режима генерации
if __name__ == "__main__":
    if (len(sys.argv) == 2 and sys.argv[1] == "--help"):
        print_how_to_start_and_exit(0)
    if (len(sys.argv) == 1):
        demo_key_generation()
        exit(0)
    print("Wrong usage!")
    print_how_to_start_end_exit()


# Примеры ввода-вывода программы
# Заходим в папку sandbox.
# python3 ../Anderson/generation.py --help
# Select Programs/sandbox directory
# Usage python3 ../Anderson/generation.py --help
# Usage python3 ../Anderson/generation.py
# 15
# Секретный ключ злоумышленника 0b10111001001
# Открытый ключ (17, 289796191)
# Закрытый ключ (102266369, 289796191)
#
# Также в файлах backdoor_key.txt private_key.txt public_key.txt сохранены данные для их дальнейшего использования.
# cat backdoor_key.txt
# 0b10111001001
# cat private_key.txt
# 0b110000110000111011000000001 0b10001010001011111000001011111
# cat public_key.txt
# 0b10001 0b10001010001011111000001011111

