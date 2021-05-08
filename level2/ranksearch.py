from itertools import combinations
from bisect import bisect_left


def make_all_cases(separate_info):
    cases = []
    for k in range(5):
        for condition in combinations([0,1,2,3], k):
            case = []
            for idx in range(4):
                if idx not in condition:
                    case.append(separate_info[idx])
                else:
                    case.append('-')
            cases.append(''.join(case))
    return cases


def solution(info, query):
    answer = []
    info_dic = {}
    for i in info:
        sep_i = i.split()
        cases = make_all_cases(sep_i)
        for case in cases:
            if case not in info_dic.keys():
                info_dic[case] = [int(sep_i[4])]
            else:
                info_dic[case].append(int(sep_i[4]))
    for key in info_dic.keys():
        info_dic[key].sort()

    for q in query:
        sep_q = q.split(' and ')
        sep_q += sep_q.pop().split(' ')
        qstr = ''
        for sq in sep_q[:4]:
            qstr += sq
        if qstr in info_dic.keys(): # binary search
            answer.append(len(info_dic[qstr]) - bisect_left(info_dic[qstr], int(sep_q[4]), lo=0, hi=len(info_dic[qstr])))
        else:
            answer.append(0)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
