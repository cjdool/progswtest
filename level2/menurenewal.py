from itertools import combinations


def solution(orders, course):
    answer = []
    for cnt in course:
        dic = {}
        for order in orders:
            if cnt > len(order):
                continue
            ordlist = list(order)
            for case in combinations(ordlist, cnt):
                c = ''.join(sorted(case))
                if c in dic:
                    dic[c] += 1
                else:
                    dic[c] = 1
        if len(dic) != 0:
            maxval = max(dic.values())
            if maxval > 1:
                for key, val in dic.items():
                    if val == maxval:
                        answer.append(key)

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))