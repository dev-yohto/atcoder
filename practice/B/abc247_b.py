N = int(input())
A = []

for _ in range(N):
    full_name = input().split()
    A.append(full_name)

for i in range(N):
    ctn_s = 0
    ctn_t = 0
    for j in range(N):
        if A[j].count(A[i][0]) == 1:
            ctn_s += 1
        if A[j].count(A[i][1]) == 1:
            ctn_t += 1
        if ctn_s > 1 and ctn_t > 1:
            print("No")
            exit()

print("Yes")
