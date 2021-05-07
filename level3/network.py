from collections import deque


def bfs(graph, visited, start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        x = queue.popleft()
        for nx, nval in enumerate(graph[x]):
            if nval == 1 and visited[nx] == 0:
                queue.append(nx)
                visited[nx] = 1
    return


def solution(n, computers):
    answer = 0
    visited = [0] * n
    while True:
        start = -1
        for idx, v in enumerate(visited):
            if v == 0:
                start = idx
                break
        if start == -1:
            break
        else:
            bfs(computers, visited, start)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
