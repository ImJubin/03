'''
크루스칼
모든 간선들 보면서
가중치 가장 작은 간선부터 고르자(정렬)
이때, 사이클 발생하면 pass


'''

def find_set(x):    # 대표자 검색
    if x == parents[x]:
        return x

    # return find_set(parents[x]) # 경로 압축 해주자. e에 직접 대표자 저장하도록 만들자.
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):    #
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 사이클 방지
    if ref_x == ref_y:
        return              # 같다면 하지 말고,

    # 일정한 규칙으로 연결하자.
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y  # 아니면 합쳐라


V, E = map(int, input().split())
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    #간선에 대한 정보 저장
    edges.append((start, end, weight))

edges.sort(key=lambda  x: x[2])     # 가중치 기준으로 오름차순
parents = [i for i in range(V)]     # make_set (정점 기준으로 만들어준다)

#작은 것부터 고르면서 나아가자
#언제까지? N-1 선택할 때까지
cnt = 0         # 현재까지 선택한 간선의 수
result = 0      # MST 가중치의 합

for u, v, w in edges:
    # u와 v가 연결이 안되어 있으면 선택
    # == 다른 집합이라면 연결
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        result += w

        if cnt == V - 1:        #mst 구성이 끝났다.
            break

print(result)

