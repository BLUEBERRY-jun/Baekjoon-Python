A=int(input())
B=int(input())

one = B % 10
ten = (B // 10) % 10
hun = B // 100

print (A * one)
print (A * ten)
print (A * hun)
print (A * B)