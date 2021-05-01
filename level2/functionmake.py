from collections import deque


def solution(progresses, speeds):
    answer = deque([])
    for pro, s in zip(progresses, speeds):
        remain = 100 - pro
        if remain%s == 0:
            answer.append(remain//s)
        else:
            answer.append(remain//s + 1)

    result = []
    while answer:
        pivot = answer.popleft()
        if not answer:
            result.append(1)
        else:
            flag = True
            idx = 1
            for nxt in answer:
                if nxt > pivot:
                    result.append(idx)
                    flag = False
                    break
                idx += 1
            if flag:
                result.append(idx)
            for i in range(result[-1]-1):
                answer.popleft()
    return result

'''
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
'''

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
