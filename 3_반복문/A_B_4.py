# import sys

# while True:
#     try:
#         A, B = map(int,sys.stdin.readline().split())
#         print (A+B)
#     except:
#         break

import sys

for i in sys.stdin:
    a, b = map(int, i.split())
    print(a+b)