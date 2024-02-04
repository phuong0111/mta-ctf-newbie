from pwn import xor
from Cryptodome.Util.number import *

flag = 0x7112F78C5D4F524F35EDB74957785D2FD690484A535428DCA879404B4F24EDEE0704061D6093EE07045A

flag = long_to_bytes(flag)

pref = xor(b"MSEC{", flag)[:5]

for i in range(256):
    for j in range(256):
        key = pref + long_to_bytes(i) + long_to_bytes(j)
        try:
            mess = xor(key, flag).decode()
            print(mess)
        except Exception:
            pass
