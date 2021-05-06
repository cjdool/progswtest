def solution(number, k):
    answer = number
    n = len(number)
    idx = 0
    while k > 0 and idx < n-1:
        x = answer[idx]
        y = answer[idx+1]
        if int(x) < int(y):
            answer = answer[:idx] + answer[idx+1:]
            k -= 1
            idx = 0
        else:
            idx += 1
    if k > 0:
        answer = answer[:-k]

    return answer

print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))
print(solution('987654', 3))
print(solution('123456', 3))

# 4177252841, 4 -> 77252841, 2 -> 7752841, 1 -> 775841, 0