import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            return answer

        if scoville:
            second = heapq.heappop(scoville)
            new = first + 2*second
            answer += 1
            heapq.heappush(scoville, new)

    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))