# import sys
# x = [1, 1, 2, 2, 2, 8]
# y = list(map(int, input().split()))

# result = []
# for i in range(6):
#     value = x[i]-y[i]
#     result.append(value)
# print (*result)


# import sys
# x = [1, 1, 2, 2, 2, 8]
# y = list(map(int, input().split()))

# result = [x[i]-y[i] for i in range(6)]
# print (*result)


# import sys
# x = [1, 1, 2, 2, 2, 8]
# y = list(map(int, input().split()))

# result = []
# for a, b in zip(x, y):
#     result.append(a - b)

# print(*result)


# import sys
# x = [1, 1, 2, 2, 2, 8]
# y = list(map(int, input().split()))

# result = [a - b for a, b in zip (x, y)]

# print(*result)


# import sys
# x = [1, 1, 2, 2, 2, 8]
# y = list(map(int, input().split()))

# result = map(lambda a, b: a - b, x, y)

# print(*result)



import sys

x = [1, 1, 2, 2, 2, 8]
y =  list(map(int, sys.stdin.readline().split()))
chess_result = []

for a, b in zip(x,y):
    chess_result.append(a-b)

print (*chess_result) #zip 공식 외울것 그럼 쉬움