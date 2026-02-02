# S = input()
# alpabet = 'abcdefghijklmnopqrstuvwxyz'

# for i in alpabet:
#     print (S.find(i), end=" ")

# S=input()
# alpabet_ord = range(97, 123)

# for i in alpabet_ord:
#       char = chr(i)
#       print (S.find(char), end=" ")  





import sys
s = sys.stdin.readline().strip()
s_list = range(97, 123)

for i in s_list:
    i = chr(i)    #아스키코드를 알파벳으로 변환
    print (s.find(i), end=" ")      #count는 없을때 0 find는 -1