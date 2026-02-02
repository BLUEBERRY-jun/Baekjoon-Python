import sys
dice = list(map(int, sys.stdin.readline().split()))

if len(set(dice))==1:
    num = list(set(dice))[0]
    print (10000+num*1000)
elif len(set(dice))==2:
    dice.sort()
    num = (dice)[1]
    print (1000+num*100)
elif len(set(dice))==3:
    num = max(dice)
    print (num*100)

# set(dice)는 숫자가 아니라서 사칙연산이 불가능하다
# list tupple은 연결 반복은 가능하다
# 객체.매서드()