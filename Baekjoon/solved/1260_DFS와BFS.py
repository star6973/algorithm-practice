N, M, V = map(int, input().split(" "))

# 해당 노드에 인접한 노드의 리스트를 담는 형태로 그래프를 표현하자
graph = [[] for _ in range(N+1)]
graph[0] = [0, 0]
for i in range(M):
    s, e = map(int, input().split(" "))
    graph[s].append(e)
    graph[e].append(s)
    graph[s].sort()
    graph[e].sort()

def dfs(graph, node, visited):
    # 현재 노드를 방문 처리
    visited[node] = True
    print(node, end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for n in graph[node]:
        if not visited[n]:
            dfs(graph, n, visited)

from collections import deque
def bfs(graph, node, visited):
    queue = deque([node])

    # 현재 노드를 방문 처리
    visited[node] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        vertex = queue.popleft()
        print(vertex, end=" ")

        # 아직 방문하지 않은 인접한 원소를 큐에 삽입
        # BFS는 인접한 원소부터 탐색하기 때문에 뽑자마자 탐색
        for n in graph[vertex]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True

visited = [False for _ in range(N+1)]
dfs(graph, V, visited)
print()
visited = [False for _ in range(N+1)]
bfs(graph, V, visited)