def solve():
    _ = int(input())
    s = input()
    t = input()

    i = 0
    while i < len(s) and s[i] == "0":
        if t[i] != "0":
            return "NO"
        i += 1
    return "YES "

for _ in range(int(input())):
    print(solve())
    