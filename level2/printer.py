from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque([(x, 0) for x in priorities])
    queue[location] = priorities[location], 1
    while queue:
        cur, ck = queue.popleft()

        if any(cur < q[0] for q in queue):
            queue.append((cur, ck))
        else:
            answer += 1
            if ck == 1:
                return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))