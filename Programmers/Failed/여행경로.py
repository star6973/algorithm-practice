# ans = []
# def dfs(tickets, start, cnt, check):
#     ans.append(start)
#     print(tickets)
#     print(check)
#     if cnt == len(tickets):
#         return 1
#
#     for i in range(len(tickets)):
#         if check[i] == 0 and tickets[i][0] == start:
#             check[i] = 1
#             if dfs(tickets, tickets[i][1], cnt + 1, check):
#                 return 1
#             check[i] = 0
#     ans.pop()
#
#     return 0
#
# def solution(tickets):
#     tickets.sort()
#     check = [0] * len(tickets)
#     dfs(tickets, "ICN", 0, check)
#
#     return ans



def dfs(graph, N, path, here):
    path.append(here)

    # path값이 티켓값의 길이만큼 되면 DFS 탈출(전체)
    if len(path) == N + 1:
        return True

    # 현재 위치가 남은 route에 없으면 다시 원위치로
    if here not in graph:
        path.pop()
        return False
    # print('현재 path', path)
    # print('전체 그래프', graph)
    # print('부분 그래프', graph[here])
    for i in range(len(graph[here])):
        there = graph[here][-1]
        graph[here].pop()
        # print('pop하고 난뒤', graph)

        if dfs(graph, N, path, there):
            return True

        # print('DFS 실패')
        graph[here].insert(0, there)

    path.pop()
    return False


def solution(tickets):
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]

    for r in routes.keys():
        routes[r].sort(reverse=True)

    N = len(tickets)
    path = []

    if dfs(routes, N, path, "ICN"):
        answer = path

    return answer

print(solution([['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]))