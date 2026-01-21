# alpabet = input()

# total = 0

# for i in alpabet:
#     if i in "ABC":
#         total += 3

alphabet = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
total = 0

for i in alphabet:
    for d in dial:
        if i in d:
            total += dial.index(d)+3
print(total)