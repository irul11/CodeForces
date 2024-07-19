def solution():
    n = int(input())
    s = input()
    count = 0

    for c in s:
        if c == "U":
            count += 1
    
    if count & 1:
        return "YES"

    return "NO"


for _ in range(int(input())):
    print(solution())