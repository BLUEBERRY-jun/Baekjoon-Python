# import sys

# N, M = map(int, sys.stdin.readline().split())
# baskets = [0] * (N)

# for _ in sys.stdin:
#     i, j, k = map(int,_.split())
#     baskets[i-1:j] = [k] * (j-i+1)

# print(*baskets)





import sys
N, M = map(int,sys.stdin.readline().split())
baskets = [0] * N

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    baskets[i-1:j] = [k] * (j-(i-1))    
    #앞에 수만큼 뒤에 넣어줘야함 넣을 때 []쓸 것 

print (*baskets)