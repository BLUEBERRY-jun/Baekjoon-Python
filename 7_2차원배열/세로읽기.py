import sys

words = []
for _ in range(5):
    line = sys.stdin.readline().strip()
    words.append(line)

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end="")