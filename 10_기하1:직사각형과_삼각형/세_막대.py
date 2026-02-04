import sys

line = list(map(int, sys.stdin.readline().split()))
line.sort()

if line[0]+line[1] > line[2]:
    print(sum(line))
else:
    print ((line[0]+line[1])*2-1)