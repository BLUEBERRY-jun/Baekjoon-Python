x = input().upper()
y = list(set(x))
y.sort()

counts = []
for i in y:
    count = x.count(i)
    counts.append(count)


if counts.count(max(counts))>1:
    print("?")
else:
    max_val=max(counts) #count 안에서 가장큰값을 max_val안에 넣는다
    max_index=counts.index(max_val) #max_val값의 위치를 max_index에 넣는다
    print (y[max_index])

