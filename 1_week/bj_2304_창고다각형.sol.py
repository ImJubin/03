'''
가장 작은 창고 다각형 면적 구하기

주어진 입력값 중 위치(L) 기준으로 정렬을 하고싶다.
최댓값 기준으로 범위를 나눔
0~ 최댓값 위치까지 : 최댓값 갱신
최댓값 위치~ 끝 인덱스 : 
1) 끝인덱스부터 역순으로 최댓값 갱신
갱신될 때 높이가 바뀜. 다음 최댓값 위치 바뀔 때까지 높이가 그대로임.

2) 두번째로 큰 값찾기 : 기준 값을 제외하고, 제일 큰 값이 나오면 갱신
그 전까지 높이값 저장 (!!!)

(첫값,끝값) 바깥의 인덱스는 높이가 0임
인덱스는 0부터 시작

면적을 어떻게??? 0 0 4 4 6 6 6 ... 
for문 사용해서 싹 돌아
방문할 때마다 count 해버림
어떻게?



1. 입력값 받기
N
end_l (끝기둥위치)
max_h_sum (누적합)

2. N번에 걸쳐
L, H

end_l 찾기

max_h
max_h_sum

3. for문 
최댓값 위치 구하기
max_h = 0 으로 치고 더 높은 값치 비교해서 갱신
max_l = L 해서 최댓값 위치 저장

max_l 기준으로 좌 우 쪼개기
좌 :
최댓값 갱신 된다면 > 바뀐 높이값 저장 > 누적합

우 :
기준값을 제외한 최댓값 갱신 > max_h과 해당값이 같지 않으
i 최댓값인가?
아니면? 기존 값의 높이를 누적해서 더해줌
갱신 된다면 > 바뀐 높이값 누적해서 더해줌

'''

N = int(input())
empty = [0]*1001            #지붕 높이 저장할 리스트
end_l = 0                  # 마지막 기둥 위치 저장!!!!(이 위치범위까지 누적합 하고 끝내야함)

for _ in range(N):
    L, H = map(int, input().split())
    empty[L]= H                     # 기둥들 위치 저장

    if end_l < L:                   # 끝번째 기둥위치
        end_l = L

    max_l = 0
    max_h = 0
    for i in range(end_l+1):                          # 최댓값과 최댓값 위치 찾기
        if max_h < empty[i]:
            max_h = empty[i]
            max_l = i

    max_h_sum = 0

    max_h_left = 0
    for i in range(max_l+1):                       # 0~ 최댓값 위치까지 지붕 누적합
        if max_h_left < empty[i]:
            max_h_left = empty[i]
        max_h_sum += max_h_left
            
    max_h_right = 0                                   # 최댓값~ 끝까지 지붕 누적합
    for i in range(end_l, max_l, -1):                 # 인덱스 주의
        if max_h_right < empty[i]:            
            max_h_right = empty[i]
        max_h_sum += max_h_right

print(max_h_sum)
