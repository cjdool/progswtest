from functools import cmp_to_key


def twocmp(x, y):
    mindigit = min(len(x), len(y))
    for i in range(mindigit):
        if x[i] > y[i]:
            return -1
        elif x[i] < y[i]:
            return 1

    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0


def solution(numbers):
    answer = int(''.join(sorted(map(str, numbers), key=cmp_to_key(twocmp))))
    return str(answer)

print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0, 0, 0]))
