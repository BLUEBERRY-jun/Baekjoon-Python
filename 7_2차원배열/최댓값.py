# import sys

# M = []
# for i in range(9):
#     M.append(list(map(int, sys.stdin.readline().split())))

# max_val = -1
# max_row = 0
# max_col = 0

# for i in range(9):
#     for j in range(9):
#         if M[i][j] > max_val:
#             max_val=M[i][j]
#             max_row=i+1
#             max_col=j+1

# print(max_val)
# print(max_row, max_col)


# import sys

# M = []
# for i in range(9):
#     M.append(list(map(int, sys.stdin.readline().split())))

# Max_value = -1
# Max_x = 0
# Max_y = 0

# for i in range(9):
#     for j in range(9):
#         if M[i][j] > Max_value:
#             Max_value = M[i][j]
#             Max_x = i+1
#             Max_y = j+1

# print (Max_value)
# print (Max_x, Max_y)  # 2번째 내일 다시




import sys

M = []
for i in range(9):
    M.append(list(map(int, sys.stdin.readline().split())))

Max_value = -1
Max_x = 0
Max_y = 0

for i in range(9):
    for j in range(9):
        if M[i][j] > Max_value:
            Max_value = M[i][j]
            Max_x = i+1
            Max_y = j+1

print (Max_value)
print (Max_x, Max_y) # 3번째