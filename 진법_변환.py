# import sys

# N, B = sys.stdin.readline().split()
# print(int(N, int(B)))

import sys
N, B = sys.stdin.readline().split()
B = int(B)
table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = 0
N = N[::-1]

for i in range(len(N)):
    val = table.index(N[i])
    ans += val * (B ** i )

print (ans)