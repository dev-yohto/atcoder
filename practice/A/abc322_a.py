N = int(input())
S = input()

for i in range(N):
    if i == N - 1:
        print(-1)
    elif S[i] == "A":
        if S[i + 1] == "B":
            if S[i + 2] == "C":
                print(i + 1)
                break
