# import sys

# H, M = map(int,sys.stdin.readline().split())

# new_H = (H*60 + M - 45)//60
# new_M = (H*60 + M - 45)%60

# if new_H <0:
#     new_H= 24 + new_H

# print (new_H, new_M)

import sys

H, M = map(int, sys.stdin.readline().split())

total = (H*60 + M - 45)
new_H, new_M = divmod(total, 60)

print(new_H % 24, new_M)  

#파이썬의 % 연산은 이 시계 바늘이 돌아가는 것과 똑같이 작동합니다.
# -1 % 24 ➔ 23
# -5 % 24 ➔ 19
# -25 % 24 ➔ 23 (한 바퀴 돌고 다시 뒤로 한 칸)