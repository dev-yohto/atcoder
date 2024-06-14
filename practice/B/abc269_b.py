S = [input() for _ in range(10)]

A = 0
B = 0
C = 0
D = 0

for i in range(10):
    if "#" in S[i]:
        A = i + 1
        break

for i in range(10):
    if "#" in S[i]:
        B = i + 1

for i in range(10):
    if "#" in S[A - 1][i]:
        C = i + 1
        break

for i in range(10):
    if "#" in S[A - 1][i]:
        D = i + 1

print(A, B)
print(C, D)
