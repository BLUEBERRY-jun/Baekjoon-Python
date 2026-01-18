import sys
H, M, duration = map(int,sys.stdin.read().split())

total = H*60+M+duration
new_H, new_M = divmod(total,60)

print(new_H%24, new_M)