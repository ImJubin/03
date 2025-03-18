'''
9명 중 7명 골라 100
오름차순 출력

'''
heights = []
sum_heights = 0
for _ in range(9):
    heights.append(int(input()))
    sum_heights += heights[-1]

for i in range(9):
    temp_sum_heights = sum_heights
    temp_sum_heights -= heights[i]
    if temp_sum_heights <= 100:
        continue

    for j in range(i+1, 9):
        # print(i,j)
        if temp_sum_heights - heights[j] == 100:
            heights.pop(j)
            heights.pop(i)    # 인덱스 땡겨지므로, i, j-1 해도 됨.
            break

    if len(heights) == 7:
        break

heights.sort()
for height in heights:
    print(height)


