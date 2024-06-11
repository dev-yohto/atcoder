N = int(input())
binary = bin(N)
ctr = 0

for i in range(len(binary) - 2):
    if binary[-i - 1] == "0":
        ctr += 1
    else:
        print(ctr)
        break
