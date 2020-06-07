def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_state = []

    cnt = len(truck_weights)
    passing = []
    passed = []
    waiting = truck_weights

    while 1:
        if len(passed) == cnt:
            answer+=1
            break
        if len(waiting) == 0:
            pass
        else:
            truck = waiting[0]
            if sum(passing)+truck <= weight:
                passing.append(truck)
                truck_state.append(bridge_length)
                waiting.pop(0)
        # 리스트 값 모두 -1
        for i in range(len(truck_state)):
            truck_state[i] -= 1
        if truck_state[0] == 0:
            truck_state.pop(0)
            passing.pop(0)
            passed.append(0)
        answer+=1
    return answer

