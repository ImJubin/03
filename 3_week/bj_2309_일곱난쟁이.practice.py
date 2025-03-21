'''
1. 입력값

heights 빈리스트
    height 9번 입력받기
    heights sum = 0 
    
함수만들기
    for i (0부터 마지막 전 인덱스)
        for j (i+1부터 마지막 인덱스)
        temp_heights 깊은 복사
        temp_sum 깊은 복사

    만약 heights_sum이 100 되면 리턴

sort 해서 오름차순 정리    
'''

heights = []
heights_sum = 0


def find_heights():
    for i in range(8):
        for j in range(i+1, 9):
            temp_heights = heights
            temp_sum = heights_sum
            if temp_heights[i]+temp_heights[j] == (temp_sum - 100):
                temp_heights.pop(i)
                temp_heights.pop(j)
                return temp_heights


for _ in range(9):
    height = int(input())
    heights.append(height)
    heights_sum += height

A = find_heights()

A.sort()

for i in A:
    print (i)