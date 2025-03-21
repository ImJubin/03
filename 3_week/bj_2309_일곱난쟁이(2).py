'''
플래그 써서 j만 돌고 나오는 것을 바깥포문인 i까지 돌고 빠져나오게하는 버전
'''
heights = []
heights_sum = 0

for _ in range(9):
    height = int(input())
    heights.append(height)
    heights_sum += height
 # print(heights, heights_sum)
# print(len(heights))

flag = 0
for i in range(0,8):
    for j in range(i+1, 9):
        temp_heights = heights
        temp_heights_sum = heights_sum
        if temp_heights[i]+temp_heights[j] == temp_heights_sum - 100:
            p = temp_heights.pop(j)
            q = temp_heights.pop(i)
            flag = 1
            break
    if flag == 1:
        break

temp_heights.sort()
print(temp_heights)
for i in temp_heights:
    print(i)
