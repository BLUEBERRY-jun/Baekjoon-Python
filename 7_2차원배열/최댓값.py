# import sys

# num = list(map(int, sys.stdin.read().split()))

# print(max(num))
# print(num.index(max(num))+1)

import sys

M = []
for i in range(9):
    M.append(list(map(int, sys.stdin.readline().split())))

max_val = 0
max_row = 0
max_col = 0

for i in range(9):
    for j in range(9):
        if M[i][j] > max_val:
            max_val=M[i][j]
            max_row=i+1
            max_col=j+1

print(max_val)
print(max_row, max_col)