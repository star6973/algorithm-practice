def solution(citations):
    citations.sort()
    answer = 0

    for c in citations:
        max_citations = len([i for i in citations if c <= i])

        if c >= max_citations:
            answer = max_citations
            break
    
    return answer

citations = [3, 0, 6, 1, 5]
s = solution(citations)
print(s)