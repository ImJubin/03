'''
3줄요약

방향 하나 있는거 기준값으로
면적 = 하나방향값 * 앞뒤 값 중 더 긴 값 - 
긴 거 앞뒤 값 중 더 큰값이 다음 값이면
    i = 긴값 + 1 번째

마지막 값이면
    i = 긴값 - 5 번째

왜냐면 6각형이라 반시계방향으로 돌면 순서가 그렇게 됨.
혹은??
 i 개수가 1개일때 << 큰사각형의 세로임
 [i][1] 길이가 제일 클 때 << 큰사각형의 가로임
 큰사각형세로 좌 우 길이비교 후 다음값 혹은 마지막값 선택

 참외 수 = K * 면적

1 동
2 서
3 남
4 북

#################
1. 입력값
K
melon = []

'''

K = int(input())
melon_d = []
melon_l = []
meloncount = [0]*5
melonpair = []
minus_area = -1

minus_area_r = -1
minus_area_c = -1

dr = [0, 0, 0, 1, -1]
dc = [0, 1, -1, 0, 0]

# 6개의 좌표
rcs = []
# 최대/최소 행 번호, 최대/최소 열 번호
cur_r = cur_c = 0
min_r = min_c = float('inf')
max_r = max_c = float('-inf')

for i in range(6):
    d, l = map(int, input().split())
    melon_d.append(d)
    melon_l.append(l)
    meloncount[d] += 1

    cur_r += dr[d]*l
    cur_c += dc[d]*l
    if cur_r > max_r:
        max_r = max(max_r, cur_r)
    if cur_r < min_r:
        min_r = min(min_r, cur_r)
    if cur_c > max_c:
        max_c = max(max_c, cur_c)
    if cur_c < min_c:
        min_c = min(min_c, cur_c)

    rcs.append((cur_r, cur_c))

    # 첫 2가 발견됐을 때 빠지는 영역 구하기
    if meloncount[d] >= 2:
        melonpair.append(d)
        # print(melonpair)


r, c = -1, -1
for i in range(6):
    if min_r < rcs[i][0] < max_r and min_c < rcs[i][1] < max_c:
        r, c = rcs[i][0], rcs[i][1]


# print(max_r, max_c, min_r, min_c, r, c)
# print(rcs)
for i in range(len(melonpair)):
    if melonpair[i] == 1:
        minus_area_r = max_r - r
    if melonpair[i] == 2:
        minus_area_r = r - min_r
    if melonpair[i] == 3:
        minus_area_c = c - min_c
    if melonpair[i] == 4:
        minus_area_c = max_c - c

# print(minus_area_r, minus_area_c)
    # 빠지는 영역 구하기
minus_area = abs(minus_area_r) * abs(minus_area_c)

# 최대 너비를 구하기
max_area_l = max(melon_l)

max_area_idx = melon_l.index(max(melon_l))  #인덱스찾기


idx_l = max_area_idx-1
idx_r = max_area_idx+1
sec_l = -1

if max_area_idx == 0:
    idx_l = 5
elif max_area_idx == 5:
    idx_r = 0

# print(len(melon_l),idx_l,idx_r)
    
if melon_l[idx_l] < melon_l[idx_r]:        
    sec_l = melon_l[idx_r]

else:
    sec_l = melon_l[idx_l]

max_area =  max_area_l * sec_l

# print(max(melon_l), sec_l, minus_area)

place = max_area - minus_area

ans = K * place

print(ans)
    



#
#######################################################

'''


47600

1
2 5
3 5
1 1
4 2
1 4
4 3

17

7
1 60
3 20
1 100
4 50
2 160
3 30

ans 47600


7
4 50
2 160
3 30
1 60
3 20
1 100

47600
# '''