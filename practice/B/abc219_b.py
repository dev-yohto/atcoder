SS = [input() for i in range(3)]
T = input()
ans = ""

for i in T:
    if i == "1":
        ans += SS[0]
    elif i == "2":
        ans += SS[1]
    elif i == "3":
        ans += SS[2]

print(ans)
