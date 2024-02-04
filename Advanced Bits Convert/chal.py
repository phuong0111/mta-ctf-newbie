from secret import flag

flag = flag.strip("MSEC{").strip("}")

# output
output = "".join([bin(ord(_))[2:] for _ in flag])
print(f"{output = }")

assert len(flag) == 19