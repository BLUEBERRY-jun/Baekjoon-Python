import sys

while True:
    sides =list(map(int, sys.stdin.readline().split()))
    if sum(sides)==0:
        break
    sides.sort()
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    elif sides[1]==sides[2]==sides[0]:
        print("Equilateral")
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        print("Isosceles")
    else:
        print("Scalene")    #다음에는 set써서 해보기
