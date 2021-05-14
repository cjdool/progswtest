import heapq
import sys


inf = sys.maxsize


def dijkstra(graph, start):
    dist = [inf] * len(graph)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        current_dist, here = heapq.heappop(queue)
        for there, weight in graph[here].items():
            next_dist = dist[here] + weight
            if next_dist < dist[there]:
                dist[there] = next_dist
                heapq.heappush(queue, [next_dist, there])

    return dist


def solution(n, vertex):
    graph = [{} for _ in range(n)]
    for s, d in vertex:
        graph[s-1][d-1] = 1
        graph[d-1][s-1] = 1

    dist = dijkstra(graph, 0)
    maxval = max(dist)

    return dist.count(maxval)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))