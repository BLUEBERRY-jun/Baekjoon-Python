# import sys

# N = int(input())
# score = list(map(int, sys.stdin.readline().split()))

# M = max(score)

# for i in range(N):
#     score[i] = score[i]/M*100

# print (sum(score)/N)




import sys

N= int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))
M = max(N_list)

print(sum(N_list)*100/M/N)