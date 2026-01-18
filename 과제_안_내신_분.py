import sys

stu = list(range(31))
sukjae=list(map(int, sys.stdin.read().split()))

for i in range(len(sukjae)):
    stu.remove(sukjae[i]) #pop remove 차이

for j in stu:
    if j != 0:
        print(j)