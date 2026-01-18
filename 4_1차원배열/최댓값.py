import sys

num = list(map(int, sys.stdin.read().split()))

print(max(num))
print(num.index(max(num))+1)
