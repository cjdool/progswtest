def stos(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def stos2(time):
    h = time // 3600
    time -= h * 3600
    m = time // 60
    time -= m * 60
    s = time
    return '{0:02d}:{1:02d}:{2:02d}'.format(h, m, s)


def solution(play_time, adv_time, logs):
    answer = 0
    if play_time == adv_time:
        return '00:00:00'
    play_time = stos(play_time)
    adv_time = stos(adv_time)
    total_time = [0] * (play_time+1)
    for log in logs:
        starttime, endtime = log.split('-')
        total_time[stos(starttime)] += 1
        total_time[stos(endtime)] -= 1

    for i in range(1, play_time+1):
        total_time[i] += total_time[i-1]

    # cumulate
    for i in range(1, play_time+1):
        total_time[i] += total_time[i-1]

    maxval = total_time[adv_time]
    for starttime in range(1, play_time):
        endtime = min(starttime + adv_time, play_time)
        val = total_time[endtime] - total_time[starttime]
        if maxval < val:
            maxval = val
            answer = starttime + 1

    return stos2(answer)


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
