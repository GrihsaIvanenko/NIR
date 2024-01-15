T=31
q=23
p=37
N = p * q
e = 17
b = dict
a1 = b()
for i in range(1, T):
    try:
        a1[i * i % T].append(i)
    except:
        a1[i * i % T] = [i]
        
for i in sorted(a1.keys()):
    print(i, a1[i], "huy")

a2 = dict()
a2[7] = 2
a2[19] = 4
a2[9] = 5
a2[2] = 7
a2[25] = 8
a2[5] = 9
a2[10] = 20


def get_k_huy_by_gamma(gamma):
    for i in a1.keys():
        if gamma in a1[i]:
            return i
    raise "HUY 1"
    
def get_k_by_gamma(gamma):
    a = get_k_huy_by_gamma(gamma)
    if not a in a2.keys():
            raise "HUY 2" 
    return a2[a]

C = 0
for gamma in [3, 5, 6, 8, 9, 10, 14, 17, 21, 22, 23, 25, 26, 28]:
    a = gamma
    b = get_k_by_gamma(gamma) * a % T
    if (N - a * b) % T != 0:
        raise "HUY 3" 
    else:
        delta = (N - a * b) // T
        D = (b - a - C * T) ** 2 - 4 * T * (delta - b * C)
        print("gamma=", gamma, "; delta=", delta, "; D=", D, sep='')
    

