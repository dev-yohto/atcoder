N = int(input())
S = input()

found = False

for i in range(N):
    if i == N - 1:
        found = False
        break
    elif S[i] == "a" and S[i + 1] == "b":
        found = True
        break
    elif S[i] == "b" and S[i + 1] == "a":
        found = True
        break

if found:
    print("Yes")
else:
    print("No")
