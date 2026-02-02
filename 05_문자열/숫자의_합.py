# # N=int(input())
# # M=input()
# # total_M = 0

# # for i in range(N):
# #     total_M += int(M[i])

# # print (total_M)

# N=input()
# M=input()

# print(sum(map(int, M))) #map이 한개씩 들고온다라고 이해





import sys
N = int(sys.stdin.readline().strip())
N_list = list(map(int, sys.stdin.readline().strip()))
result = 0

for i in N_list:
    result += i

print(result)