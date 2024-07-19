def solver():
    n, m = list(map(int, input().split()))
    # print(n, m)
    arr = []
        
    for _ in range(n):
        arr.append(list(input().split()))
    
    if n == 1 and m == 1:
        return "-1"
    # print(arr)
    ans = ""
    for a in arr[1:]:
        ans += " ".join(a[1:]+[a[0]]) + "\n"
    ans += " ".join(arr[0][1:]+[arr[0][0]])
    return ans
    
result = ""
for _ in range(int(input())):
    print(solver())
# print(result)