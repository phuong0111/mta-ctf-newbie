from sympy import isprime

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
                    print(f"n chia hết cho q_candidate. Giá trị của n: {n}")
                    print(f"Giá trị của p (n/q): {p}")
                break  # Dừng lại khi tìm thấy n chia hết cho q
            else:
                # print("n không chia hết cho q_candidate")
                pass
