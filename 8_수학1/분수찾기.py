# X = int(input())
# line = 1

# while X > line:
#     X -= line
#     line += 1


# if line%2==0:
#     print(f"{X}/{line - X + 1}")
# else:
#     print(f"{line - X + 1}/{X}") 
#ai학습 어렵다....



x = int(input())

line = 1
while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    print(f"{x}/{line - x + 1}")
else:
    print(f"{line - x + 1}/{x}")