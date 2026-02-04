import sys

a, b, c = map(int, sys.stdin.read().split())

if a+b+c != 180:    #가장 까다로운 조건을 위로
    print("Error")
elif a == b == c:
    print("Equilateral")
elif a+b+c == 180 and (a==b or b==c or a==c):
    print("Isosceles")
else:
    print("Scalene")