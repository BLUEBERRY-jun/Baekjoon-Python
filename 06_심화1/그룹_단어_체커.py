# import sys

# x = int(input())
# group_word = 0

# for _ in range(x):
#     word = sys.stdin.readline().strip()

#     for i in range(len(word)-1):
#         if word[i] != word[i+1] and word[i] in word[i+1: ]:
#             break
#     else:           #else가 for문이랑 묶여있음 파이썬만 가능함
#         group_word += 1

# print (group_word)



import sys

N = int(input())

result = 0
for _ in range(N):
    M = sys.stdin.readline().strip() #strip해야함

    for i in range(len(M)-1): #마지막 전까지만 확인해야함 밑에줄에 i+1이 있잖아
        if M[i] != M[i+1] and M[i] in M[i+1:]: #==이 아니라 in
            break
    else:   #for이랑 묶여서 for문이 끝까지 실행될시 else실행
        result += 1
        
print (result)