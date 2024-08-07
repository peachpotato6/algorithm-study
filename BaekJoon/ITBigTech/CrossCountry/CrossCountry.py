T = int(input())
scoreList = dict()
freqList = dict()

for _ in range(T):
    N = int(input())
    table = list(map(int, input().split()))
    # add frequency
    for i in range(0, len(table)):
        freqList[table[i]] = 0
    for i in range(0, len(table)):
        freqList[table[i]] += 1
    
    # skip below 6
    for k in freqList.keys():
        if freqList[k] < 6:
            table[:] = (val for val in table if val != k)
    for i in range(0, len(table)):
        scoreList[table[i]] = 0
    for i in range(0, len(table)):
        scoreList[table[i]] += i
    
    # winner
    for items in scoreList.items():
        max = 0
        if max > items[1]:
            max = items[1]
        elif max == items[1]:


print(freqList.items())
print(scoreList.items())
print(table)


