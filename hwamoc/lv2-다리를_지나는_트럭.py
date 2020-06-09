from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    sum = 0
    bridge_q =  deque([0] * bridge_length)

    while bridge_q:
        time += 1
        sum -= bridge_q.pop()
        if truck_weights:
            if sum + truck_weights[0] <= weight:
                sum += truck_weights[0]
                bridge_q.appendleft(truck_weights.pop(0))
            else:
                bridge_q.appendleft(0)

    return time

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))