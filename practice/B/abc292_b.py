N, Q = map(int, input().split())
status = {}

for i in range(Q):
    E, X = map(int, input().split())
    if E == 1 and X not in status:
        status[X] = 1
    elif E == 1 and X in status:
        status[X] += 1
    elif E == 2 and X not in status:
        status[X] = 2
    elif E == 2 and X in status:
        status[X] += 2
    else:
        if X not in status or status[X] < 2:
            print("No")
        else:
            print("Yes")
