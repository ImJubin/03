'''
어떻게 ???

- 밑면 윗면 같은 값 찾아서 맞물리게 하기 > 6가지 경우
    딕셔너리 사용(밑면이 정해지면 마주보는 면 정해지기 때문)
옆면 중 최댓값 > 저장
최댓값의 합 구하기기

1. 입력
N
numnum : 주사위 마주보는 면면인덱스
stones : 주사위 열

2. 로직



입력값
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3

'''


# def cross_number(num):
#     if num == 0:
#         return 5
#     if 

numnum = {
   0:5,
   1:3,
   2:4,
   3:1,
   4:2,
   5:0
}

# numnum.get('1')
# numnum.values('1')

# fixed_number = numnum['0']
# print(fixed_number)



N = int(input())
stones = [list(map(int, input().split())) for _ in range(N)]

real_max_sum = 0

for i in range(1,7):
    bottom_number = i
    upper_number = i
    max_sum = 0

#밑면 윗면 맞물리기
    for floor in range(N):
        side_numbers = [1,2,3,4,5,6]
        bottom_idx = stones[floor].index(upper_number)
        upper_idx = numnum[bottom_idx]
        upper_number= stones[floor][upper_idx]        
        side_numbers.remove(stones[floor][bottom_idx])
        side_numbers.remove(stones[floor][upper_idx])
        print(bottom_number, upper_number, side_numbers)
        # print(stones[floor][bottom_idx],upper_number )
        # print(side_numbers)
        max_number = max(side_numbers)
        max_sum += max_number

    # print(max_sum)

    if real_max_sum < max_sum:
        real_max_sum = max_sum

    print(real_max_sum)
# a.index(max(a))
# 옆면 최댓값




