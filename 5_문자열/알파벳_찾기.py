# S = input()
# alpabet = 'abcdefghijklmnopqrstuvwxyz'

# for i in alpabet:
#     print (S.find(i), end=" ")

S=input()
alpabet_ord = range(97, 123)

for i in alpabet_ord:
      char = chr(i)
      print (S.find(char), end=" ")  

# map 기능 정확히 이해하
