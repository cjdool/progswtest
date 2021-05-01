import heapq


def solution(jobs):
    answer = 0
    totalcnt = len(jobs)
    # shortest job first
    heapq.heapify(jobs)
    waitqueue = []
    curtime = 0

    while jobs or waitqueue:
        while jobs:
            reqtime, duration = heapq.heappop(jobs)
            if reqtime > curtime:
                if waitqueue:
                    heapq.heappush(jobs, [reqtime, duration])
                    break
                else:
                    curtime = reqtime
            heapq.heappush(waitqueue, (duration, reqtime))

        if waitqueue: # not needed
            duration, reqtime = heapq.heappop(waitqueue)
            curtime += duration
            answer += curtime - reqtime

    return answer // totalcnt

print(solution([[0, 3], [1, 9], [2, 6]]))
