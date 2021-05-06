def solution(numbers, target):
    answer = 0
    stack = []
    stack.append((0, target))
    while stack:
        idx, t = stack.pop()
        if idx == len(numbers):
            if t == 0:
                answer += 1
        else:
            stack.append((idx+1, t-numbers[idx]))
            stack.append((idx+1, t+numbers[idx]))

    return answer

print(solution([1, 1, 1, 1, 1], 3))