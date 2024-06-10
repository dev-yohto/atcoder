S = input()
j = True
k = False
l = False
for i in range(len(S)):
    if S.count(S[i]) != 1:
        j = False
        break
    if S[i].islower() == True:
        k = True
    if S[i].isupper() == True:
        l = True
if j == True and k == True and l == True:
    print("Yes")
else:
    print("No")
