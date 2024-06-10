N, X = map(int, input().split())
alphaList = [chr(i) for i in range(65, 91)]
i = X // N
j = X % N
if j == 0:
    print(alphaList[int(i) - 1])
else:
    print(alphaList[int(i)])
