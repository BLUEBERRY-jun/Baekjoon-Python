# import sys

# N, X = map(int, sys.stdin.readline().split())
# num = list(map(int, sys.stdin.readline().split()))

# for i in num:
#     if i < X:
#         print (i, end=" ")













import sys
N, X = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

for i in N_list:
    if i < X:
        print(i, end=" ")