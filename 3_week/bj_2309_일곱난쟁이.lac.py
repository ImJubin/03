'''
9명 중 7명 골라 100
오름차순 출력
팝, 인덱스 j부터 빼서 뒤에서부터 빼기

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
            heights.pop(j)    # 순서 바꾸어서 뒤부터 빼기.그럼 i 영향 안미치니까.(j, i)
            heights.pop(i)    # 인덱스 땡겨지므로, i, j-1 해도 됨.
            break

    if len(heights) == 7:
        break

heights.sort()
for height in heights:
    print(height)


