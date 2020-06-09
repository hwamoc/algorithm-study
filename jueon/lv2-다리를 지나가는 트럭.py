#개션 필요.. 방법을 찾아보는 중입니다. 
def solution(bridge_length, weight, truck_weights):
    time = 0 
    road=[0]*bridge_length
    while road:
        time=time+1
        road.pop(0)
        if truck_weights:
            if sum(road)+truck_weights[0]<=weight:
                road.append(truck_weights.pop(0))
            else: road.append(0)
    return time