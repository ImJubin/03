

def prim(start_node):
    pq = [(0, start_node)]  # 시작점은 가중치가 0이다.
    MST = [0] * V  # N개를 모두 연결했을 때 종료 , visited와 동일.
    min_weight = 0  # 최소 비용 저장

    while pq:
        weight, node = heapq.heappop(pq)

        # 이미 방문한 노드를 뽑았다면 continue
        if MST[node]:
            continue

        MST[node] = 1   # 방문 처리
        min_weight += weight    # 누적합 추가


        for next_node in range(V):
            # 갈 수 없으면 pass
            if graph[node][next_node] == 0:
                continue
            # 이미 방문 했으면 pass
            if MST[next_node]:
                continue

            heapq.heappush(pq, (graph[node][next_node], next_node))


import heapq

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight

result = prim(0)    #최소 비용 바꾸어도 동일
print(f'최소비용 = {result}')

