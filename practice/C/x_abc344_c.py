N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

ans = {}

for i in range(Q):
    found = False
    for j in range(N):
        if X[i] >= A[j]:
            for k in range(M):
                if X[i] >= A[j] + B[k]:
                    for l in range(L):
                        if A[j] + B[k] + C[l] == X[i]:
                            ans[i] = "Yes"
                            found = True
                            break
                    if found:
                        break
            if found:
                break
    if not found:
        ans[i] = "No"

for i in range(Q):
    print(ans[i])
