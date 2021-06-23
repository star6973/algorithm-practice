import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)

    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break

        second = hq.heappop(scoville)
        hq.heappush(scoville, first + (second * 2))
        answer += 1

    # heap = []
    # for i, sc in enumerate(scoville):
    #     heapq.heappush(heap, sc)
    
    # first_min_scoville = -1
    # while True:
    #     if len(heap) != 1:
    #         first_min_scoville = heapq.heappop(heap)
    #         second_min_scoville = heapq.heappop(heap)
    #     else:
    #         first_min_scoville = heapq.heappop(heap)
    #         if first_min_scoville < K:
    #             answer = -1
    #         break
        
    #     if first_min_scoville >= K:
    #         break

    #     new_scoville = first_min_scoville + (second_min_scoville * 2)
    #     heapq.heappush(heap, new_scoville)
    #     answer += 1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
s = solution(scoville, K)
print(s)