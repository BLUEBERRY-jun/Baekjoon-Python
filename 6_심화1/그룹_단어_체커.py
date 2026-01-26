import sys

x = int(input())
group_word = 0

for _ in range(x):
    word = sys.stdin.readline().strip()

    for i in range(len(word)-1):
        if word[i] != word[i+1] and word[i] in word[i+1: ]:
            break
    else:           #else가 for문이랑 묶여있음 파이썬만 가능함
        group_word += 1

print (group_word)
