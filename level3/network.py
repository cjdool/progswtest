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
    start = 0
    while 0 in visited:
        if visited[start] == 0:
            bfs(computers, visited, start)
            answer += 1
        start += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
