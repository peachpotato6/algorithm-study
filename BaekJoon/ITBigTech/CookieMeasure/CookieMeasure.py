N = int(input())

head = []

# head 찾기
for i in range(N):
    rows = input().strip()
    if "*" in rows:
        head.append(i+2)
        head.append(rows.index("*")+1)
        break

left_hand = 0
right_hand = 0
waist = 0
left_leg = 0
right_leg = 0

for i in range(head[0]-1, N):
    rows = input().strip()
    # 팔 길이
    if i == head[0]-1:
        for j in range(head[1]-1):
            if "*" == rows[j]:
                left_hand += 1
        for j in range(head[1], len(rows)):
            if "*" == rows[j]:
                right_hand += 1
    # 허리 길이
    elif rows.index("*") == head[1]-1:
        waist += 1
    # 다리 길이
    elif "*" in rows[head[1]-2] and "*" in rows[head[1]]:
        left_leg += 1
        right_leg += 1
    elif "*" in rows[head[1]-2]:
        left_leg += 1
    elif "*" in rows[head[1]]:
        right_leg += 1
    


print(head[0],head[1])
print(left_hand, right_hand, waist, left_leg, right_leg)


            
    

    