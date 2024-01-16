import sys
sys.path.append('../common/')

from evklid import calc_inverse
from file_funcs import write_line_to_file

from common import gen

def factorize(n):
    i = 2
    result = []
    while True:
        while n % i == 0:
            result.append(i)
            n //= i
        i = i + 1
        if i * i >= n:
            break
    if n != 1:
        result.append(n)
    return result

def calc_t(A):
    byte_len = 1
    assert A >= 10
    while True:
        if (2 ** (byte_len - 1) <= A and A < 2 ** byte_len):
            break
        byte_len = byte_len + 1
    assert byte_len % 3 == 0
    return byte_len * 4 // 3

def calc_private_key(backdoor_key, e, n):
    t = calc_t(backdoor_key)
    n_small = n % backdoor_key
    n_factorisation = factorize(n_small)
    assert(len(n_factorisation) == 2)
    p_small, q_small = n_factorisation[0], n_factorisation[1]
    p = gen(p_small, backdoor_key, t)
    q = gen(q_small, backdoor_key, t)
    fi_n = (p - 1) * (q - 1)
    d = calc_inverse(e, fi_n)
    print(f"Закрытый ключ ({d}, {n})")
    write_line_to_file(bin(d) + " " + bin(n), "cracked_private_key.txt")

def setup(backdoor_key_file, public_key_path):
    backdoor_data = backdoor_key_file.readlines()
    assert len(backdoor_data) == 1
    backdoor_key = int(backdoor_data[0], 2)
    public_key_data = public_key_path.readlines()
    assert len(public_key_data) == 1
    e_as_line, n_as_line = public_key_data[0].split()
    e, n = int(e_as_line, 2), int(n_as_line, 2)
    calc_private_key(backdoor_key, e, n)

def setup_with_default():
    backdoor_key_file = open("backdoor_key.txt", "r")
    public_key_path = open("public_key.txt", "r")
    setup(backdoor_key_file, public_key_path)

def setup_with_keys(backdoor_key_path, public_key_path):
    backdoor_key_file = open(backdoor_key_path, "r")
    public_key_path = open(public_key_path, "r")
    setup(backdoor_key_file, public_key_path)

# Интерфейс пользователя. Инструкция по использованию.
def print_how_to_start_and_exit(exit_code = 1):
        print("Select Programs/sandbox directory")
        print("Usage python3 ../Anderson/encrypt.py --help")
        print("Usage python3 ../Anderson/encrypt.py")
        print("Usage python3 ../Anderson/encrypt.py *backdoor_key_path* *public_key_path*")
        exit(exit_code)

# Запуск демо-режима злоумышленника
if __name__ == "__main__":
    if (len(sys.argv) == 2 and sys.argv[1] == "--help"):
        print_how_to_start_and_exit(0)
    if (len(sys.argv) == 1):
        setup_with_default()
        exit(0)
    if (len(sys.argv) == 3):
        setup_with_keys(sys.argv[1], sys.argv[2])
        exit(0)
    print("Wrong usage!")
    print_how_to_start_end_exit()

# Примеры ввода-вывода программы
# Заходим в папку sandbox.
# python3 encrypt.py --help
# Select Programs/sandbox directory
# Usage python3 ../Anderson/encrypt.py --help
# Usage python3 ../Anderson/encrypt.py
# Usage python3 ../Anderson/encrypt.py *backdoor_key_path* *public_key_path*
#
# python3 ../Anderson/encrypt.py
# Закрытый ключ (24218047022184955043770602818166588113, 102926699844286058956324438494402130367)
# Важно чтобы в папке запуска были файлы backdoor_key.txt public_key.txt, иначе программа не запустится!
#
# Переходим в другую папку
# cd ../Anderson
# python3 encrypt.py ../sandbox/backdoor_key.txt ../sandbox/private_key.txt
# Закрытый ключ (17, 102926699844286058956324438494402130367)
# Попробуем по закрытому ключу получить открытый. Получилось.
