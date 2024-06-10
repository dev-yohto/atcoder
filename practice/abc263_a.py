cards = list(map(int, input().split()))
counter = 0
for i in range(len(cards)):
    counter += cards.count(cards[i])
if counter == 13:
    print("Yes")
else:
    print("No")
