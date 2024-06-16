from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

numbers_dict = defaultdict(int)
for i in A:
    numbers_dict[i] += 1

print(len(numbers_dict))
