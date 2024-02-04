from mysecrets import a, b, n, flag

def f(x):
    return [(a * ord(i) + b) % n for i in x]

P = f(flag)
with open("enc.txt", "w") as f:
    f.write(str(P))
