import math


ctxt = [
    180,
    234,
    326,
    199,
    158,
    269,
    69,
    142,
    304,
    142,
    77,
    15,
    323,
    304,
    15,
    296,
    104,
    150,
    15,
    269,
    142,
    150,
    15,
    31,
    50,
    104,
    15,
    296,
    69,
    69,
    23,
    15,
    323,
    204,
    285,
]


def f(x, a, b, n):
    p = [(a * i + b) % n for i in x]
    return p


def reverse_f(x, a, b, n):
    p = [((pow(a, -1, n) * (_ - b)) % n) for _ in x]
    return p


p = list(set(ctxt))
# print(p)

__gcd = []
for a in p:
    for b in p:
        for c in p:
            for d in p:
                try:
                    __gcd.append(math.gcd(a - b, b - c, c - d))
                except Exception:
                    pass
__gcd = list(set(__gcd))

for a in __gcd:
    for b in range(1, 400):
        for n in range(304, 400):
            try:
                p = reverse_f(ctxt, a, b, n)
                check = True
                for _ in p:
                    if _ < 32 or _ > 126:  # char co the in duoc
                        check = False
                        break
                if check:
                    p = "".join([chr(_) for _ in p])
                    if "MSEC" in p:
                        print(p)
            except Exception:
                pass
