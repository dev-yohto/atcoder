X, Y = map(int, input().split())
if Y > X and 2 >= Y - X:
    print("Yes")
elif X > Y and -3 <= Y - X:
    print("Yes")
else:
    print("No")
