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

'''
def dfs(graph, root, end, traps):
    res = []
    visited = []
    stack = [(root, 0)]

    while stack:
        n, curweight = stack.pop()
        if n == end:
            res.append(curweight)
        if n not in visited or n in traps:
            if n in traps:

            else:
                visited.append(n)
                for nxt, weight in graph[n].items():
                    stack.append((nxt, curweight+weight))

    return min(res)
'''


def solution(n, start, end, roads, traps):
    graph = [{} for _ in range(n)]
    graph2 = [{} for _ in range(n)]
    for p, q, s in roads:
        if q-1 in graph[p-1].keys():
            graph[p-1][q-1] = min(s, graph[p-1][q-1])
            graph2[p-1][q-1] = min(s, graph2[p-1][q-1])
        else:
            graph[p-1][q-1] = s
            graph2[p-1][q-1] = s
        if p-1 in graph2[q-1].keys():
            graph2[q-1][p-1] = min(s, graph2[q-1][p-1])
        else:
            graph2[q-1][p-1] = s

    dist = dijkstra(graph, start-1)
    dist2 = dijkstra(graph2, start-1)

    answer = 0
    if dist[end-1] != inf:
        answer += dist[end-1]
    if dist2[end-1] != inf:
        answer += dist2[end-1]

    return answer

print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3]))
