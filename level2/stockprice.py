from collections import deque


def solution(prices):
    answer = list(range(len(prices)-1, -1, -1))
    prices = deque(prices)

    for idx in range(len(answer)):
        price = prices.popleft()
        for i, item in enumerate(prices):
            if item < price:
                answer[idx] = i+1
                break

    return answer


print(solution([1, 2, 3, 2, 3]))