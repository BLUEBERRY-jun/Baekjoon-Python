N = int(input())
d = 2

while N > 1:
    if N % d == 0:
        print(d)
        N //= d
    else:
        d += 1