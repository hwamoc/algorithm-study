def solution(bridge_length, weight, truck_weights):
    answer = 0
    temp = 0
    total_trucks=len(truck_weights)
    for i, truck in enumerate(truck_weights):
        temp+=truck
        answer+=1
        
        if temp>weight:
            temp=0
            answer+=bridge_length
            
        elif i == total_trucks-1:
            temp = 0
            answer+=bridge_length
    return answer