# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#     x = sys.stdin.readline().strip()
#     print(x[0] + x[-1])




import sys
T = int(sys.stdin.readline())
T_list = []

for _ in range(T):
    T_list = list(sys.stdin.readline().strip()) 
    #\n까지 입력받아서 strip으로 삭제해야함
    print (T_list[0]+T_list[-1])