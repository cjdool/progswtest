def solution(places):
    answer = []
    for place in places:
        retval = 1
        plist = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    plist.append((i, j))

        for i in range(len(plist)):
            if retval == 1:
                pivotx, pivoty = plist[i]
                for j in range(i+1, len(plist)):
                    x, y = plist[j]
                    mandist = abs(pivotx-x) + abs(pivoty-y)
                    if mandist == 1:
                        retval = 0
                        break
                    elif mandist == 2:
                        if x == pivotx - 2 and y == pivoty and place[pivotx-1][pivoty] == 'X':
                            continue
                        elif x == pivotx - 1 and y == pivoty + 1 and place[pivotx-1][pivoty] == 'X' and place[pivotx][pivoty+1] == 'X':
                            continue
                        elif x == pivotx and y == pivoty + 2 and place[pivotx][pivoty+1] == 'X':
                            continue
                        elif x == pivotx + 1 and y == pivoty + 1 and place[pivotx+1][pivoty] == 'X' and place[pivotx][pivoty+1] == 'X':
                            continue
                        elif x == pivotx + 2 and y == pivoty and place[pivotx+1][pivoty] == 'X':
                            continue
                        elif x == pivotx + 1 and y == pivoty - 1 and place[pivotx+1][pivoty] == 'X' and place[pivotx][pivoty-1] == 'X':
                            continue
                        elif x == pivotx and y == pivoty - 2 and place[pivotx][pivoty-1] == 'X':
                            continue
                        elif x == pivotx - 1 and y == pivoty - 1 and place[pivotx-1][pivoty] == 'X' and place[pivotx][pivoty-1] == 'X':
                            continue
                        else:
                            retval = 0
                            break

        answer.append(retval)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
