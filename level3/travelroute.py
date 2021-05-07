def dfs(startport, retic):
    if not retic:
        return [startport]

    candid = []
    for src, dst in retic:
        if src == startport:
            candid.append((src, dst))

    candid.sort(key=lambda x: x[1])
    for cansrc, candst in candid:
        retic.remove([cansrc, candst])
        ret = dfs(candst, retic)
        if ret:
            return [startport] + ret
        else:
            retic.append([cansrc, candst])

    return []


def solution(tickets):
    return dfs('ICN', tickets)


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
