# N =  int(input())
# num = list(map(int, input().split()))
# v = int(input())

# print (num.count(v))



import sys
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print (N_list.count(v)) #2회차