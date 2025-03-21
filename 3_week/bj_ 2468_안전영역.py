'''

'''

dr=[]
dc=[]
N= int(input())
graph= [list(map(int, input().split())) for _ in range(N)]
visited = []
heights =set()
answer = max_height = 1     # 아무지역도 물에 안 잠길 수 있다.

for row in range(N):
    heights.update(graph[row])
max_height = max(heights)

def dfs(r, c, h):
    visited[r][c] = 1
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:
            continue

        if graph[nr][nc]:
            continue

        



for height in heights:
    if height == max_height:
        continue

    area_count = 0
    visited = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if graph[r][c] > height and not visited[r][c]:
                area_count += 1
                dfs(r, c, height)

    answer = max(answer, area_count)

print(answer)

