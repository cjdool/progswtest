def solution(citations):
    answer = 0
    maxvalue = max(citations)
    count = [0] * (maxvalue+1)
    for cit in citations:
        count[cit] += 1
    for i in range(maxvalue-1, -1, -1):
        count[i] += count[i+1]
    for h in range(maxvalue-1, -1, -1):
        if h <= count[h]:
            answer = h
            break

    return answer


print(solution([3, 0, 6, 1, 5]))

'''

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
'''