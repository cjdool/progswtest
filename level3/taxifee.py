import heapq
import sys

inf = sys.maxsize


def dijkstra(graph, K):
    dist = [inf] * len(graph)
    dist[K] = 0
    queue = []
    heapq.heappush(queue, [0, K])
    while queue:
        current_dist, here = heapq.heappop(queue)
        for there, weight in graph[here].items():
            next_dist = dist[here] + weight
            if next_dist < dist[there]:
                dist[there] = next_dist
                heapq.heappush(queue, [next_dist, there])

    return dist


def solution(n, s, a, b, fares):
    answer = inf
    graph = [{} for _ in range(n)]
    for c,d,f in fares:
        graph[c-1][d-1] = f
        graph[d-1][c-1] = f

    distmap = []
    for i in range(n):
        dist = dijkstra(graph, i)
        distmap.append(dist)

    for k in range(n):
        answer = min(answer, distmap[s-1][k] + distmap[k][a-1] + distmap[k][b-1])

    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
