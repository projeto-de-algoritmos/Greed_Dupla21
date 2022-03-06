t = int(input())

for _ in range(t):
    n = int(input())
    
    tasks = [None] * n

    for i in range(n):
        start, end = map(int, input().split())
        tasks[i] = (end, start)

    tasks.sort()
    max_tasks = [(0,0)]
    count = 0
    for j in tasks:
        if j[1] >= max_tasks[count][0]:
            max_tasks.append(j)
            count += 1
    print(count)

        

        