N = int(input())
A = list(map(int, input().split()))
numbers = []

for i in range(1, N + 1):
    numbers.append(i)

sorted_A = sorted(A)

if numbers == sorted_A:
    print("Yes")
else:
    print("No")
