N, weightLimit = map(int, input().split())

items = [None] * N
for i in range(N):
    value, weight = map(int, input().split())
    items[i] = ((value/weight), value, weight)

items.sort(reverse=True)

totalValue = 0
for item in items:
    weight = item[2]
    value = item[1]
    if (weightLimit - weight) > -1:
        totalValue += value
        weightLimit -= weight
    else:
        totalValue += value * (weightLimit / weight)
        break

print(totalValue)