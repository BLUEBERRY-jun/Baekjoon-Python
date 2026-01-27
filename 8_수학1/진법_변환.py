# import sys

# N, B = sys.stdin.readline().split()
# print(int(N, int(B)))

# import sys
# N, B = sys.stdin.readline().split()
# B = int(B)
# table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ans = 0
# N = N[::-1]

# for i in range(len(N)):
#     val = table.index(N[i])
#     ans += val * (B ** i )

# print (ans)




# import sys

# N, B = sys.stdin.readline().split()
# B = int(B)

# print (int(N, B))



import sys

N, B = sys.stdin.readline().split()
B = int(B)
table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
x = 0
result = 0

for i in range(len(N)):
    x = table.index(N[i])
    result += x * (B ** i)  #B에 진법 

print (result)  #2번쨰 