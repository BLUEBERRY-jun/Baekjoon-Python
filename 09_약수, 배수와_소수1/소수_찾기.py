import sys

N = int(sys.stdin.readline())
x_list = map(int, sys.stdin.readline().split())

result = 0
for num in x_list:
    if num < 2:
        continue
    for j in range(2,int(num**0.5)+1):
        if num % j == 0:
            break
    
    else:   #tab한번 하면 소수의 개수를 셀 수 있다
        result += 1

print (result)  #제곱근 사용하는거 ai 도움 받음

# 제곱근 약수의 짝꿍 원리 1 36, 2 18, 3 12, 4 9, 6 6, 9 4, 12 3, 18 2, 36 1 
# 이렇게 짝꿍있어서 두번해 볼 필요없이 반으로 나눠서 해보면 되서 제곱근 + 1 해서 나누자