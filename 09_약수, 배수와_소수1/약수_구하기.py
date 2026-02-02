import sys

N, K = map(int, sys.stdin.readline().split())
N_list = []

for i in range (1, N+1):
    if N % i == 0:
        N_list.append(i)

if len(N_list) < K:
    print(0)
else:
    print(N_list[K-1])
