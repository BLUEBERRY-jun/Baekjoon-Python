import sys

num = list(map(int, sys.stdin.read().split()))
result = []

for i in num:
    result.append(i % 42)

print (len(set(result)))