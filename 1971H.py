def solution():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    d = [[0, 0] for _ in range(n+1)]

    for ori in [a, b, c]:
        for i in range(n):
            if ori[i] > 0:
                d[abs(ori[i])][0] += 1
            else:
                d[abs(ori[i])][1] += 1
    # print(d)
    neg = 0        
    for i in range(len(d)):
        neg += min(d[i])

        if neg > n:
            return "NO"

    return "YES"


test = ""
for _ in range(int(input())):
    test += solution() + "\n"
print(test[:-1])

