# import sys

# grade_to_score = {
#     "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
#     "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

# total_score = 0
# total_credit = 0

# for _ in range(20):
#     data = sys.stdin.readline().split()
#     if not data: break

#     credit = float(data[1])
#     grade = data[2]

#     if grade == "P":
#         continue

#     total_score += credit * grade_to_score[grade]
#     total_credit += credit

# print ("{:.6f}".format(total_score/total_credit))



# import sys

# grade_to_score = {
#      "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
#      "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0} #{}딕셔너리

# total_score = 0
# total_credit = 0

# for i in range(20):
#     data = sys.stdin.readline().split()

#     credit = float(data[1]) #실수형
#     grade = data[2]

#     if grade == "P":
#         continue
    
#     total_score += credit * grade_to_score[grade]
#     total_credit += credit

# print ("{:.6f}".format(total_score/total_credit)) #format 쓰는법





import sys

grade_to_score = {
     "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
     "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

data = []
credit_s = 0
result = 0

for _ in range(20):
    data = sys.stdin.readline().split()
    credit = float(data[1])
    grade = data[2]
    if grade == "P":
        continue
    result += credit * grade_to_score[grade]
    credit_s += credit

print("{:.6f}".format(result/credit_s))