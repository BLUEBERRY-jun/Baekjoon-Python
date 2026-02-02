# N = int(input())
# x=1
# y=1
# i=0
# while True:
#     if x >= N:
#         break
#     i += 1
#     y += 1
#     x += 6*i

    
# print (y)




N = int(input())

line = 1
x = 1
i = 0

while True:
    if x >= N:
        break
    else:
        line += 1
        i += 1
        x += 6*i

print (line)