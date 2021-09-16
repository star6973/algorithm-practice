N = int(input())
M = int(input())

graph = {0: []}
for i in range(1, M+1):
    a, b = map(int, input().split())
    if a not in graph.keys():
        graph[a] = [b]
    else:
        graph[a].append(b)
    
    if b not in graph.keys():
        graph[b] = [a]
    else:
        graph[b].append(a)

def dfs(graph, node, visited):
    visited[node] = True
    for n in graph[node]:
        if not visited[n]:
            dfs(graph, n, visited)

visited = [False] * (N+1)
dfs(graph, 1, visited)

print(len([v for v in visited if v == True]) - 1)