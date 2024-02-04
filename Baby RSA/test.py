from sympy import isprime
from Crypto.Util.number import *

# Số a đã cho
a = 80010678722841069804372512802456615676374598635439671916170512885067569296605399657233599421856535796385681607868510909937338841790332071846857268291

# Giá trị m đã cho
m = 488594150018356104743360471780205403545441209060256729137164038537676599362878190981920516554421590258238515618449750985891175030926717331209498982161611981924927571937232980671860995692342844980196870803553484460965923405826239739612544997270974984272106618470669107922303287837996978131051615925495644837

# Duyệt qua giá trị của k từ 2^15 đến 2^16 - 1
for k in range(2**15, 2**16):
    q_candidate = k * (2**496) + a

    # Kiểm tra xem q_candidate có phải là số nguyên tố hay không
    if isprime(q_candidate):
        # print(f"Đã tìm thấy q: {q_candidate}")
        # print("k =", k)

        # Duyệt qua giá trị của h từ 0 đến 255
        for h in range(256):
            # Tính giá trị n từ m và h
            n = (m << 8) + h

            # Kiểm tra n chia hết cho q
            if n % q_candidate == 0:
                p = n // q_candidate
                if isprime(p):
                    print(f"{n = }")
                    print(f"{p = }")
                    print(f"q = {q_candidate}")
                    enc = 0x260772A51CABF4DB2AD87F563EBC1A7F1329D28900F1C2350F36B586B4D50E85EBDE64E5F547D9FE28FA90B1D1C1108E80452639D7D3560B2F161EA82625C8CEF3D8C2E881E1B010ECE2CE0C8F574180B2CC75D193C3006A95B1360D998EFA62E2B8F1496E61E44FC7B45F518EE1B8C237D46A151283B0AA704888F9A80AD376
                    d = pow(0x10001, -1, (p - 1) * (q_candidate - 1))
                    print(f"{pow(enc, d, n)}")
                    print(long_to_bytes(pow(enc, d, n)))
                break  # Dừng lại khi tìm thấy n chia hết cho q
            else:
                # print("n không chia hết cho q_candidate")
                pass
