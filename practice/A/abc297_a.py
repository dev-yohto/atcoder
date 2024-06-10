N, D = map(int, input().split())
T = list(map(int, input().split()))
ctr = 0
for i in range(N - 1):
    if T[i + 1] - T[i] <= D:
        print(T[i + 1])
        break
    ctr += 1

if ctr == N - 1:
    print(-1)
