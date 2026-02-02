# import sys

# x, y = sys.stdin.readline().split()
# x = int(x[::-1])
# y = int(y[::-1])

# if x-y>0:
#     print(x)
# elif x-y<0:
#     print(y)

# print(max(x, y))





import sys
a, b = map(int,sys.stdin.readline().split())

a = int(str(a)[::-1])
b = int(str(b)[::-1])

if a > b:
    print(a)
else:
    print(b)