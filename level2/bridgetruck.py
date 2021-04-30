from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridgequeue = deque()
    bridgetotalweight = 0
    truckqueue = deque(truck_weights)
    while truckqueue or bridgequeue:
        if bridgequeue:
            outtruck, trucktime = bridgequeue.popleft()
            if answer - trucktime == bridge_length:
                bridgetotalweight -= outtruck
            else:
                bridgequeue.appendleft((outtruck, trucktime))
        if truckqueue:
            truck = truckqueue.popleft()
            if bridgetotalweight + truck > weight:
                truckqueue.appendleft(truck)
            else:
                bridgequeue.append((truck, answer))
                bridgetotalweight += truck
        answer += 1

    return answer


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))