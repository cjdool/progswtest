from collections import deque

def solution(arr, k):
    answer = 1000
    n = len(arr)
    ansstatestr = ''.join(map(str, list(range(1,n+1))))
    queue = deque()
    startstatestr = ''.join(map(str, arr))
    queue.append((startstatestr , 0))
    visited = {startstatestr : 1}

    while queue:
        curstatestr, cnt = queue.popleft()

        if curstatestr == ansstatestr:
            answer = min(answer, cnt)
            continue

        curstate = list(curstatestr)

        maxval = '1'
        for x in range(n, 0, -1):
            if curstate[x-1] != str(x):
                maxval = str(x)
                break
        maxidx = curstate.index(maxval)

        for kv in range(1, k+1):
            if maxidx + kv < n:
                curstate[maxidx], curstate[maxidx + kv] = curstate[maxidx + kv], curstate[maxidx]
                nxtstatestr = ''.join(curstate)
                if nxtstatestr not in visited:
                    queue.append((nxtstatestr, cnt+1))
                    visited[nxtstatestr] = 1
                curstate[maxidx + kv], curstate[maxidx] = curstate[maxidx], curstate[maxidx + kv]

    return answer


print(solution([4,5,2,3,1], 2))