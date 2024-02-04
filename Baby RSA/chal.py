from Cryptodome.Util.number import bytes_to_long, long_to_bytes, getStrongPrime

p, q = getStrongPrime(512), getStrongPrime(512)
n = p * q
e = 65537

FLAG = open("flag.txt", "r").read().strip().encode()

FLAG = bytes_to_long(FLAG)

enc = hex(pow(FLAG, e, n))
print(f"_n = {n >> 8}")
print(f"_q = {q % 2**(512-16)}")
print(f"enc = {enc}")
