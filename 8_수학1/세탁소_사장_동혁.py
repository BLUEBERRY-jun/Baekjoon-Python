# T = int(input())

# quarter = 0
# dime = 0
# nickel = 0
# penny = 0

# for i in range(T):
#     x = int(input())
#     quarter = x // 25
#     x %= 25
#     dime = x // 10
#     x %= 10
#     nickel = x//5
#     x %= 5
#     penny = x//1
    
#     print(quarter, dime, nickel, penny, end=" ")
#     print()


T = int(input())
coins = [25,10,5,1]

for _ in range(T):
    x = int(input())
    
    result = []
    for coin in coins:
        result.append(x//coin)
        x %= coin
        
    print (*result)