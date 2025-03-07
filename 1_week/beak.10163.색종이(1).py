'''
N
squre
areas

면적에 들어가서, 한칸씩 체크함
그거 N장마다 세줄거임 > 다 받고 나서 영역 돌아줘야함.
그래서 빈 도화지 필요함.(squre)
1111 넣을 빈리스트 필요함 = areas

 1장일 때. 11111 표시 > area에 넣음
 2장일 때. 2222 표시 > a~
 3장일 때. 3333 > a~
 n장일 때. nnn > a~
		

# 출력    

# '''

N = int(input())
square = [[0]*1001 for _ in range(1001)]
areas = [0]*(N+1)


for count in range(1,N+1):
    arr = list(map(int, input().split()))
    
    for i in range(arr[0],arr[0]+arr[2]):
        for j in range(arr[1],arr[1]+arr[3]):
            square[i][j] = count

for i in range(1001):
    for j in range(1001):
        areas[square[i][j]] += 1
        
for i in range(1,N+1): ###쌤한테물어보기

    print(areas[i])