# import sys

# N, B = map(int, sys.stdin.readline().split())
# table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# result = ""

# while N > 0 :
#     result += table[N % B]
#     N //= B

# print (result[::-1])


import sys

N, B = map(int, sys.stdin.readline().split())
table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

x = 0
result = ""
while N > 0:
    x = N % B 
    N = N // B
    result += table[x]  #string은 append 불까

print(result[::-1])   #처음 몫이 1의자리 수이기 떄문에 뒤집어줘야함
#2번째