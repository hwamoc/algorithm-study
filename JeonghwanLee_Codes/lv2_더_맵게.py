import heapq

def check_over(scoville, K):
    if scoville[0]>K:
        return True
    else:
        return False


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while(not check_over(scoville, K)):
            min_1 = heapq.heappop(scoville)
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville,min_1+min_2*2)
            count+=1
            
            if len(scoville) is 1:
                if scoville[0]<K:
                    return -1
                else:
                    return count
        
    return count