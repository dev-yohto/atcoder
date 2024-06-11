abc = input()
new_abc = [abc[i] for i in range(len(abc))]
ans = 0
for i in range(3):
    num = new_abc[0] + new_abc[1] + new_abc[2]
    ans += int(num)
    new_abc.append(new_abc[0])
    del new_abc[0]

print(ans)
