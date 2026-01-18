import sys

N, M = map(int, sys.stdin.readline().split())
baskets = [0] * (N)

for _ in sys.stdin:
    i, j, k = map(int,_.split())
    baskets[i-1:j] = [k] * (j-i+1)

print(*baskets)