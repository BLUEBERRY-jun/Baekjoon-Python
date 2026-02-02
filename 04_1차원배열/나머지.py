# import sys

# num = list(map(int, sys.stdin.read().split()))
# result = []

# for i in num:
#     result.append(i % 42)

# print (len(set(result)))




import sys
result_list = set()
x = list(map(int, sys.stdin.read().split()))

for i in range(10):
    result_list.add(x[i]%42)

print(len(result_list))