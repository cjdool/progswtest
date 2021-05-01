from itertools import permutations


def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    else:
        i = 3
        while i*i <= n:
            if n % i == 0:
                return False
            i += 2
        return True


def solution(numbers):
    answer = 0
    numberlist = list(numbers)
    visited = []
    for i in range(1, len(numbers)+1):
        for case in permutations(numberlist, i):
            num = int(''.join(case))
            if num not in visited and isprime(num):
                answer += 1
            visited.append(num)
    return answer


print(solution("17"))
print(solution("011"))
