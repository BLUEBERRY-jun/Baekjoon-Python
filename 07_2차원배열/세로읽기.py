# import sys

# words = []
# for _ in range(5):
#     line = sys.stdin.readline().strip()
#     words.append(line)

# for j in range(15):
#     for i in range(5):
#         if j < len(words[i]):
#             print(words [i][j], end="")


# import sys

# words = []
# for _ in range(5):
#     words.append (sys.stdin.readline().strip())
    
# for j in range(15):
#     for i in range(5):
#         if j < len(words[i]):
#             print(words [i][j], end="")  # 2번째 내일 다시


import sys

words = []

for i in range(5):
    words.append(list(sys.stdin.readline().strip()))

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end="")  #3번째