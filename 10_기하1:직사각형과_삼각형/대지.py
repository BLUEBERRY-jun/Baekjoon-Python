import sys

x = int(sys.stdin.readline())

A_list = []
B_list = []
for _ in range(x):
    A, B =map(int, sys.stdin.readline().split())
    A_list.append(A)
    B_list.append(B)

result = (max(A_list)-min(A_list))*((max(B_list))-(min(B_list)))
print(result)