'''

    7985. Rooted Binary Tree 재구성

    성삼 회사에서 마지막 면접을 보게 된 당신에게 Rooted Binary Tree 재구성이라는 미션으로 주었다.
    먼저 Rooted tree란 트리의 정점 중 하나가 root로 정해지고 간선의 양 끝점이 부모, 자식 관계를 맺게 만든 것이다.
    Rooted binary tree는 그 중에서 이진 트리(binary tree)를 의미한다.
    주어지는 정보는 tree를 중위 순회(inorder traversal)한 결과이다.

    일반적으로 중위 순회(inorder traversal)를 통해 기존의 트리를 완벽히 복구하는 것이 불가능하다.
    가능한 경우가 다양하기 때문이다.
    따라서 성삼 회사에서는 tree가 항상 완전 이진 트리를 제공한다고 하였다.
    높이가 K이며 정점의 개수가 2K-1인 tree를 의미한다.

    중위 순회(inorder traversal)란 위와 같은 트리가 있을 때 L->T->R순으로 순회하는 것을 말한다.
    따라서 위의 트리의 중위 순회(inorder traversal)한 결과는 3-2-7-5-6-1-4 이다.

    당신은 면접에서 레벨 별로 정점 번호를 왼쪽부터 순서대로 대답해야 한다.
    트리의 깊이와 중위 순회(inorder traversal) 결과를 줬을 때, 올바르게 대답하여서 면접에 합격하자.

'''

# import heapq
#
# T = int(input())
# for t in range(T):
#     K = int(input())
#     tree = list(map(int, input().split()))
#     print(heapq.heapify(tree))
#     heap = []
#     for t in tree:
#         heapq.heappush(heap, t)
#
#     for h in heap:
#         print(heapq.heappop(h))


# def solution(n):
#     f = [0 for _ in range(n+1)]
#     f[0] = 1
#     f[1] = 2
#     for i in range(1, n+1):
#         f[i] = f[i-1] + f[i-2]
#     return f[n]
#
# print(solution(3) % 1000000007)