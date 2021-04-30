def solution(answers):
    answer = []
    cntlist = [0, 0, 0]
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    for i, ans in enumerate(answers):
        if ans == pattern1[i%5]:
            cntlist[0] += 1
        if ans == pattern2[i%8]:
            cntlist[1] += 1
        if ans == pattern3[i%10]:
            cntlist[2] += 1

    maxval = max(cntlist)
    for i, cn in enumerate(cntlist):
        if maxval == cn:
            answer.append(i+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))