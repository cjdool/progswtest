import heapq as hq


def solution(operations):
    answer = [0, 0]
    queue = []
    for operation in operations:
        cmd, num = operation.split()
        if cmd == 'I':
            hq.heappush(queue, int(num))
        else:
            if queue and num == '1':
                queue.remove(max(queue))
                hq.heapify(queue)
            if queue and num == '-1':
                hq.heappop(queue)

    if queue:
        answer[0] = max(queue)
        answer[1] = min(queue)

    return answer



print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I 7","I 5","I 5","D -1", "D 1"]))