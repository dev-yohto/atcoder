N = int(input())
A = list(map(int, input().split()))
ans = []

for i in range(N - 1):
    ans.append(A[i])
    diff = A[i] - A[i + 1]
    if abs(diff) != 1:
        if diff < 0:
            for j in range(abs(diff) - 1):
                ans.append(A[i] + 1 + j)
        elif diff > 0:
            for j in range(diff - 1):
                ans.append(A[i] - 1 - j)
ans.append(A[N - 1])

print(*ans)
