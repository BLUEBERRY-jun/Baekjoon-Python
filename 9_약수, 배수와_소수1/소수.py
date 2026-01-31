import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

sosu = []
for i in range(M, N+1):
    if i < 2:
        continue

    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        sosu.append(i)

if not sosu:
    print(-1)
else:
    print (sum(sosu))
    print (min(sosu))
