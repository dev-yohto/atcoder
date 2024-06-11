N, L = map(int, input().split())
A = list(map(int, input().split()))
ctr = 0
for i in range(N):
    if A[i] >= L:
        ctr += 1
print(ctr)
