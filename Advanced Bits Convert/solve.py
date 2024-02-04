import time


output = "111001011001011100011101010111100101001001001001110111110011101011111110100110100111011111100110010011111010110110011100001100001"

candidate = []
tmp = []

maxLength = len(output)


def get_flag(idx: int, tmp: list):
    if idx < maxLength:
        if output[idx] == "1":
            if idx + 6 <= maxLength:
                _ = tmp.copy()
                _.append(output[idx : idx + 6])
                get_flag(idx + 6, _)
            if idx + 7 <= maxLength:
                _ = tmp.copy()
                _.append(output[idx : idx + 7])
                get_flag(idx + 7, _)
        else:
            pass
    else:
        if len(tmp) == 19:
            candidate.append("".join([chr(int(_, 2)) for _ in tmp]))


get_flag(0, tmp)
print(candidate)
