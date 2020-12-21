'''

    [문제 설명]
    주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.
    항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

    [제한사항]
    모든 공항은 알파벳 대문자 3글자로 이루어집니다.
    주어진 공항 수는 3개 이상 10,000개 이하입니다.
    tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
    주어진 항공권은 모두 사용해야 합니다.
    만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
    모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

    [입출력 예]
    tickets	                                                            return
    [[ICN, JFK], [HND, IAD], [JFK, HND]]	                            [ICN, JFK, HND, IAD]
    [[ICN, SFO], [ICN, ATL], [SFO, ATL], [ATL, ICN], [ATL,SFO]]	        [ICN, ATL, ICN, SFO, ATL, SFO]

    [입출력 예 설명]
    예제 #1
        [ICN, JFK, HND, IAD] 순으로 방문할 수 있습니다.

    예제 #2
        [ICN, SFO, ATL, ICN, ATL, SFO] 순으로 방문할 수도 있지만 [ICN, ATL, ICN, SFO, ATL, SFO] 가 알파벳 순으로 앞섭니다.

'''

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