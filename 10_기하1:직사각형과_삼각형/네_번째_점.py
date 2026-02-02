import sys
x_list = []
y_list = []

for _ in range(3):
    x, y =  map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i])==1:
        ans_x = x_list[i]
    if y_list.count(y_list[i])==1:
        ans_y = y_list[i]

print(ans_x, ans_y) #^사용해서도 해보기
#3009번