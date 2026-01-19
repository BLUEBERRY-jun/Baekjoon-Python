import sys

N,M = map(int, sys.stdin.readline().split())
baskets = list(range(N+1))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    baskets[i:j+1] = baskets[i:j+1][::-1]

print(*baskets[1:])