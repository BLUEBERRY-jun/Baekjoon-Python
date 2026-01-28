# import sys

# A, B, V = map(int,sys.stdin.readline().split())
# day = 1

# while V > 0:
#     V = V - A
#     if V <= 0:
#         break
#     else:
#         V = V + B
#         day += 1

# print(day)    #수가 많으면 오류남

import sys

A, B, V = map(int,sys.stdin.readline().split())

day = (V-B-1)//(A-B) + 1

print(day)