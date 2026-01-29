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

# import sys

# A, B, V = map(int,sys.stdin.readline().split())

# day = (V-B-1)//(A-B) + 1    #올림 매서드 안쓰고 수식으로 해결하는 법

# print(day)






import sys

A, B ,V = map(int, sys.stdin.readline().split())

x = V - A #올라갈양
A - B #올라갔다 잔거임 이건

print ((V-B-1)//(A-B)+1)