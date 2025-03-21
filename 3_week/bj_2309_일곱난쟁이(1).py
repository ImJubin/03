'''
함수 쓰는 버전.

0. 어떻게 풀어?
이중포문 활용,
2개 값 빼줘서 100이 되면 break
i 값 고정하고, j가 i값 제외한 모든 난쟁이 빼준다.
100이 안된다면 다음 j 값을 찾고, 100이 되면 break
원본보존을 위해 카피떠놓기

1. 입력
height = 9번 입력받기
heights 빈 리스트에 입력값 추가
heights_sum 입력값 누적합해주기

2. 로직
이중포문 활용,
2개 값 빼줘서 100이 되면 break

3. 출력
오름차순 출력
sort
'''


def height_find():
    for i in range(0,8):
        for j in range(i+1, 9):
            temp_heights = heights
            temp_heights_sum = heights_sum
            if temp_heights[i]+temp_heights[j] == temp_heights_sum - 100:
                temp_heights.pop(i)
                temp_heights.pop(j)
                return temp_heights
            print(temp_heights[i],temp_heights[j])

heights = []
heights_sum = 0


for _ in range(9):
    height = int(input())
    heights.append(height)
    heights_sum += height
 # print(heights, heights_sum)
# print(len(heights))

A = height_find()

A.sort()
for i in A:
    print(i)




        # if i>j:
        #     break
        # if 
        

        # print()
        # temp_heights.pop(j)
        # temp_heights.pop(i)
        
        # if temp_heights_sum == 100:
        #     break
        # if len(temp_heights) == 7:
            
        #     print(temp_heights)
        #     break
        # if i < 0 and i > len(heights) and j < 0 and j > len(heights) and i >= j:
        #     break

    # print(temp_heights)
       