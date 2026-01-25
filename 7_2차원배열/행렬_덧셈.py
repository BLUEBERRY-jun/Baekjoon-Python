import sys

N, M = map(int, sys.stdin.readline().split())

matrix_A=[]
for i in range(N):
    matrix_A.append(list(map(int, sys.stdin.readline().split())))

matrix_B=[]
for i in range(N):
    matrix_B.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        print(matrix_A[i][j]+matrix_B[i][j],end=" ")
    print()

    #ai로 공부