S = input()
L = ""
for i in range(len(S)):
    j = -i - 1
    if S[j] == "6":
        L += "9"
    elif S[j] == "9":
        L += "6"
    else:
        L += S[j]
print(L)
