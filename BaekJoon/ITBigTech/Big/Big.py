N = int(input())

people = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    rank = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank = rank + 1
    if i == N-1:
        print(rank)
    else:
        print(rank, end=" ")
    

            
