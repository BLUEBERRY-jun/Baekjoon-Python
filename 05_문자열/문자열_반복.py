# import sys


# T= int(sys.stdin.readline())
# for _ in range(T):
#     result=""           #""chr형 0int형
#     R, S = sys.stdin.readline().split()
#     R = int (R)
#     for i in S:
#         result += i*R

#     print(result)





import sys
s = int(sys.stdin.readline())

for _ in range(s):
    r, p = sys.stdin.readline().split()
    r = int(r)
    for i in p:
        print(i*r,end="")
    print()