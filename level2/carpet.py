def solution(brown, yellow):
    total = brown + yellow
    for b in range(1, total+1):
        if total % b == 0 and b <= total//b:
            a = total // b
            if 2*a+2*(b-2) == brown:
                return [a, b]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
