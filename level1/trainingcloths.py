def solution(n, lost, reserve):
    tra = [1] * n
    for l in lost:
        tra[l-1] -= 1
    for r in reserve:
        tra[r-1] += 1
    for idx, t in enumerate(tra):
        if t > 1:
            if idx > 0 and tra[idx-1] == 0:
                tra[idx-1] = 1
                tra[idx] = 1
            elif idx < n-1 and tra[idx+1] == 0:
                tra[idx+1] = 1
                tra[idx] = 1

    return n - tra.count(0)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
