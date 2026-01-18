import sys

N, X = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

for i in num:
    if i < X:
        print (i, end=" ")