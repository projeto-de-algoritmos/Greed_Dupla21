import heapq

n = int(input())
cows = [None] * n

for i in range(n):
    galoons, deadline = map(int, input().split())
    cows[i] = (galoons, deadline)

# job sequencing greedy algorithm

cows.sort(key=lambda x: x[1])
solution = 0
heap = []

for i in range(n - 1, -1, -1):
    if i == 0:
        slots = cows[i][1]
    else:
        slots = cows[i][1] - cows[i - 1][1]
    
    heapq.heappush(heap, (-cows[i][0], cows[i][1]))

    while slots and heap:
        galoons, deadline = heapq.heappop(heap)
        slots -= 1
        solution += galoons

print(solution*-1)