N = input()
flg = True

for i in range(len(N)):
    if i == len(N) - 1:
        break
    if int(N[i]) <= int(N[i + 1]):
        flg = False
        break
if flg:
    print("Yes")
else:
    print("No")
