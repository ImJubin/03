def bfs(start_node):
    q = [start_node]

    while q:
        now = q.pop(0)

        print(now, end = '')

        for next_node in graph[now]:

            if visited[next_node]:
                continue

            visited[next_node] = 1
            q.append(next_node)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

