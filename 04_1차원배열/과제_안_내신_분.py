# import sys

# stu = list(range(31))
# sukjae=list(map(int, sys.stdin.read().split()))

# for i in range(len(sukjae)):
#     stu.remove(sukjae[i]) #pop remove 차이

# for j in stu:
#     if j != 0:
#         print(j)




#set으로 차집합, for zip, remove로 가능함
import sys
x_list = range(1,31)
y_list = list(map(int,sys.stdin.read().split()))
result_list = list(set(x_list)-set(y_list))
result_list.sort()

for i in result_list:

    print(i)
