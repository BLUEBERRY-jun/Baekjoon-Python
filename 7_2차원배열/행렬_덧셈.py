# import sys

# N, M = map(int, sys.stdin.readline().split())

# matrix_A=[]
# for i in range(N):
#     matrix_A.append(list(map(int, sys.stdin.readline().split())))

# matrix_B=[]
# for i in range(N):
#     matrix_B.append(list(map(int, sys.stdin.readline().split())))

# for i in range(N):
#     for j in range(M):
#         print(matrix_A[i][j]+matrix_B[i][j],end=" ")
#     print()

    #ai로 공부

# import sys

# N, M = map(int, sys.stdin.readline().split())

# matrix_x = []
# matrix_y = []

# for i in range (N):
#     matrix_x.append(list(map(int, sys.stdin.readline().split())))

# for j in range (N):
#     matrix_y.append(list(map(int, sys.stdin.readline().split())))

# for i in range(N):
#     for j in range(M):
#         print(matrix_x[i][j]+matrix_y[i][j],end=" ")
#     print () # 2번째 내일 다시


import sys

N, M = map(int, sys.stdin.readline().split())

list_x = []
list_y = []


for i in range(N):
    list_x.append(list(map(int, sys.stdin.readline().split())))

for j in range(N):
    list_y.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        print (list_x[i][j] + list_y[i][j], end=" ")
    print () #3번째

