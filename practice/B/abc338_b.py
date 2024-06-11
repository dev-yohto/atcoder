from collections import defaultdict

s = input()
d = defaultdict(int)

for i in s:
    d[i] += 1

max_keys = [k for k, v in d.items() if v == max(d.values())]

sorted = sorted(max_keys)

print(sorted[0])
