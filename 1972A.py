def solution():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0
    
    for i in range(n):
        if a[i] > b[i]:
            result += 1
            a = a[:i] + [b[i]] + a[i:n-1]

    return result


for _ in range(int(input())):
    print(solution())
