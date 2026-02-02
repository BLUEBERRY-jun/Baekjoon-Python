# import sys

# N,M = map(int, sys.stdin.readline().split())
# baskets = list(range(N+1))

# for _ in range(M):
#     i, j = map(int, sys.stdin.readline().split())
#     baskets[i:j+1] = baskets[i:j+1][::-1] #[이상:미만]

# print(*baskets[1:])




import sys

N, M = map(int,sys.stdin.readline().split())
N_list = list(range(N+1))

for _ in range(M):
    x, y = map(int,sys.stdin.readline().split())
    N_list[x:y+1] = N_list[x:y+1][::-1]

print(*N_list[1:])