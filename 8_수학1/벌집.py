# N = int(input())

# x=1
# y=1

# while N > x:
#     x += 6 * y
#     y += 1

# print (y)



N = int(input())
x=1
y=1
i=0
while True:
    if x > N:
        break
    i += 1
    y += 1
    x += 6*i

    
print (y)