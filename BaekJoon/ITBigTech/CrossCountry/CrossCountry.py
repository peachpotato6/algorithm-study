T = int(input())
score_list = dict()
freq_list = dict()
five_list = dict()

for _ in range(T):
    N = int(input())
    table = list(map(int, input().split()))
    # add frequency
    for i in range(0, len(table)):
        freq_list[table[i]] = 0
    for i in range(0, len(table)):
        freq_list[table[i]] += 1
    
    # skip below 6
    for k in freq_list.keys():
        if freq_list[k] < 6:
            table[:] = (val for val in table if val != k)
    for i in range(0, len(table)):
        score_list[table[i]] = 0

    # freqList 초기화해서 4번째 빈도까지 저장하는 리스트로 사용    
    for i in range(0, len(table)):
        freq_list[table[i]] = 0
    
    # 4번째까지만 더해야함
    for i in range(0, len(table)):
        if freq_list[table[i]] < 4:
            score_list[table[i]] += i+1
            freq_list[table[i]] += 1
        # 5번째 five_list에 저장
        if freq_list[table[i]] == 4:
            five_list[table[i]] = i+1
        
    # winner
    for items in score_list.items():
        # 5번째랑 비교해서 5번째 점수가 높은 items[1]을 출력
        if max(set(score_list.values())) == items[1]:
            print(max(five_list, key=five_list.get))
        else:
            print(max(score_list, key=score_list.get))

print(freq_list.items())
print(score_list.items())
print(table)


