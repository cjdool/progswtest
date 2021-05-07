def solution(N, number):
    dp = []
    for i in range(1, 9):
        case_set = {int(str(N)*i)}
        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(x*y)
                    if y != 0:
                        case_set.add(x//y)

        if number in case_set:
            return i

        dp.append(case_set)

    return -1

print(solution(5, 12))
print(solution(2, 11))