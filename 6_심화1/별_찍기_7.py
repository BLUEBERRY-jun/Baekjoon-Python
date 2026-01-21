'''
N = int(input())

for i in range(2*N):
    if i % 2 == 0:
        continue
    else:
        result = "*"*i
        print(f"{result:^{2*N-1}}".rstrip())


for i in range(2*N-2,0,-1):
    if i % 2 == 0:
        continue
    else:
        result = "*"*i
        print(f"{result:^{2*N-1}}".rstrip())
'''

'''
n = int(input())

for i in range (1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))
for i in range (n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))
'''

# n = int(input())
# lines = []

# for i in range (1, n+1):
#     lines.append(" " * (n-i) + "*" * (2*i-1))

# ans = lines + lines[:-1][::-1]
# print(*ans, sep="\n")


N = int(input())

j = -1
lines = []
for i in range (N):
    j += 2
    lines.append(" "*(N-1-i)+"*"*j)

print(*lines + lines[:-1][::-1], sep="\n")    