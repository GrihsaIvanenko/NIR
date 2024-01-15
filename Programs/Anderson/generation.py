import sys
sys.path.append('../common/')

from gen_prime import gen_prime_with_fix_len
from evklid import calc_inverse
from rabin_miller import miller_rabin as check_simple
from file_funcs import write_line_to_file

def gen_secret_key(t):
    len_A = t * 3 // 4
    A = gen_prime_with_fix_len(len_A)
    return A

def gen(x_small, A, t):
    k = gen_prime_with_fix_len(t // 4, x_small)
    X = None
    while X is None:
        if check_simple(A * k + x_small, t):
            X = A * k + x_small
        else:
            k = k + 1
    return X


def gen_keys(t, A):
    len_small = t // 4
    p_small, q_small = -1, -1
    while p_small == q_small:
        p_small = gen_prime_with_fix_len(len_small)
        q_small = gen_prime_with_fix_len(len_small)
    p = gen(p_small, A, t)
    q = gen(q_small, A, t)
    n = p * q
    fi_n = (p - 1) * (q - 1)
    # Не предполагается работа с такими маленькими числами. 
    # Если fi_n не более 4 бит, то p_small - 1битное число, а раз простое, то хотя бы 2.
    assert fi_n > 17
    e = 17
    d = calc_inverse(e, fi_n)
    return e, d, n

def demo_key_generation():
    print("Введите 1 число t - число бит в числах p и q. Обычно используют 256, 512, 1024, 2048, 4096")
    t = int(input())
    A = gen_secret_key(t)
    print(f"Секретный ключ злоумышленника {bin(A)}")
    write_line_to_file(bin(A), "backdoor_key.txt")
    e, d, n = gen_keys(t, A)
    print(f"Открытый ключ ({e}, {n})")
    print(f"Закрытый ключ ({d}, {n})")
    write_line_to_file(bin(e) + " " + bin(n), "public_key.txt")
    write_line_to_file(bin(d) + " " + bin(n), "private_key.txt")

def print_how_to_start_and_exit(exit_code = 1):
        print("Select Programs/sandbox directory")
        print("Usage python3 ../Anderson/generation.py --help")
        print("Usage python3 ../Anderson/generation.py gen_keys")
        exit(exit_code)
        
# Запуск демо-режима генерации 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        printf("Wrong usage!")
        print_how_to_start_and_exit()
    if (sys.argv[1] == "--help"):
        print_how_to_start_and_exit(0)
    if (sys.argv[1] == "gen_keys"):
        demo_key_generation()
        exit(0)
    print_how_to_start_end_exit()


# Примеры ввода-вывода программы
