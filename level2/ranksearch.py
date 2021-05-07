def solution(info, query):
    answer = []
    for q in query:
        qlist = q.split(' and ')
        qlist += qlist.pop().split(' ')
        cnt = 0
        for i in info:
            ilist = i.split(' ')
            if qlist[0] == '-' or qlist[0] == ilist[0]:
                if qlist[1] == '-' or qlist[1] == ilist[1]:
                    if qlist[2] == '-' or qlist[2] == ilist[2]:
                        if qlist[3] == '-' or qlist[3] == ilist[3]:
                            if int(qlist[4]) <= int(ilist[4]):
                                cnt += 1
        answer.append(cnt)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
