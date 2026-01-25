'''
word = input()

x=list(word)
y=x[::-1]

if x == y:
    print("1")    
else :
    print("0")

'''

'''
word = input()

x=list(word)
n=len(x)
palindrome=True

for i in range(n // 2):
    if x[i] != x[n-1-i]:
        palindrome=False
        break

if palindrome:
    print("1")
else:
    print("0")
    
'''

# word = input()

# x=list(word)
# left = 0
# right = len(x)-1
# palindrome=1

# while left<right:
#     if x[left]!=x[right]:
#         palindrome=0
#         break
#     left += 1
#     right -= 1

# print (palindrome)


# alphabet = input()

# result = 1
# N=len(alphabet)//2

# for i in range(N):
#     if alphabet[i]==alphabet[-(1+i)]:
#         continue
#     elif alphabet[i]!=alphabet[-(1+i)]:
#         result = 0
#         break

# print (result)



import sys

word = list(sys.stdin.readline().strip()) #strip으로 마지막에 있는 \n삭제

result = 1 #0으로 하면 a한글자일때 0으로 출력되서 안됨
for i in range(len(word)//2):
    if word[i] == word[::-1][i]: #word[::-1][i] word[i][::-1] 차이 인지
        result = 1
    else:
        result = 0
        break

print (result)

#다음엔 for문 없이 만들어 볼것