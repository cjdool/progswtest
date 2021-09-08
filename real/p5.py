from itertools import combinations


def dfs(start, visited, edges, case):
    stack = [start]
    visited[start] = True
    cnt = 1

    while stack:
        cur = stack.pop()
        for idx, (edgex, edgey) in enumerate(edges):
            if idx not in case:
                if edgex == cur and not visited[edgey]:
                    stack.append(edgey)
                    visited[edgey] = True
                    cnt += 1
                elif edgey == cur and not visited[edgex]:
                    stack.append(edgex)
                    visited[edgex] = True
                    cnt += 1

    return cnt


def solution(n, edges):
    for case in combinations(list(range(n-1)), 2):
        visitied = [False] * n
        p1 = dfs(0, visitied, edges, case)
        if p1 != n//3:
            continue
        p2 = dfs(visitied.index(False), visitied, edges, case)
        if p2 != n//3:
            continue
        return list(case)


print(solution(9, [[0,2], [2,1], [2,4], [3,5], [5,4], [5,7], [7,6], [6, 8]]))
print(solution(3, [[1,0], [1,2]]))

