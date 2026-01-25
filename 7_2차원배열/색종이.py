import sys

N =  int(sys.stdin.readline())

paper = []
for _ in range(100):
    row = [0] * 100
    paper.append(row) # 100 100 짜리 배열 만듬

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    for i in range(x, x+10):
        for j in range(y,y+10):
            paper[i][j]=1 #입력받은 x,y값을 1로 바꿔서 저장

total_area = 0
for row in paper:
    total_area += row.count(1)
print(total_area) 
# paper.count(1)는 1을 직접 들고 있는게 아니라 하나씩 꺼내서 세야함