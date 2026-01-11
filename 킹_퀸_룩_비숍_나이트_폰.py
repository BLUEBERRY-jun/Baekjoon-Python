fix = list(map(int, input().split()))
origin = [1, 1, 2, 2, 2, 8]

result = (a - b for a, b in zip(origin , fix))
print(*result)