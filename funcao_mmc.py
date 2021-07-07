def mcc(a, b):
    n = 1
    c = a
    while (a % b) != 0:
        a = c * n
        n = n + 1
    return a

print(mcc(5, 10))