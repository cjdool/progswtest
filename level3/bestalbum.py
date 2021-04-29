from functools import cmp_to_key


def twocmp(x, y):
    if x[0] > y[0]:
        return 1
    elif x[0] == y[0]:
        if x[1] > y[1]:
            return -1
        elif x[1] < y[1]:
            return 1
        else:
            return 0
    else:
        return -1


def solution(genres, plays):
    answer = []
    dic = {}
    dic2 = {}
    for idx, (gen, p) in enumerate(zip(genres, plays)):
        if gen in dic:
            dic[gen] += p
            dic2[gen].append((p, idx))
        else:
            dic[gen] = p
            dic2[gen] = [(p, idx)]

    sortdict = sorted(dic.items(), key=(lambda x: x[1]), reverse=True)
    for key, val in sortdict:
        playcntlist = dic2[key]
        playcntlist.sort(key=cmp_to_key(twocmp), reverse=True)
        answer.append(playcntlist[0][1])
        if len(playcntlist) != 1:
            answer.append(playcntlist[1][1])

    return answer

'''
def solution2(genres, plays):
    answer = []
    dic = {e:[] for e in set(genres)}
    for idx, (gen, p) in enumerate(zip(genres, plays)):
        dic[gen].append((p, idx))
    genreSort = sorted(list(dic.keys()), key= lambda x: sum(map(lambda y: y[0], dic[x])), reverse=True)
    for g in genreSort:
        temp = [e[1] for e in sorted(dic[g], key= lambda x: (x[0], -x[1]), reverse=True)]
        answer += temp[:min(len(temp), 2)]
    return answer
'''

print(solution(["classic", "pop", "classic", "classic", "pop", "classic"], [500, 600, 150, 800, 2500, 500]))