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

word = input()

x=list(word)
left = 0
right = len(x)-1
palindrome=1

while left<right:
    if x[left]!=x[right]:
        palindrome=0
        break
    left += 1
    right -= 1

print (palindrome)
