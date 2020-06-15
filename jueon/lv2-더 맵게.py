
def solution(scoville, K):
    import heapq
    answer = 0
    
    # #1차 풀이 (정확성: 57.1 효율성 23.8 81/1)
#     heapq.heapify(scoville)
#     while (scoville[0]<K):
#         n1=heapq.heappop(scoville)
#         n2=heapq.heappop(scoville)
        
#         heapq.heappush(scoville, n1+n2*2)
        # answer+=1
        
        
    #2차 풀이 100/100
    
#     heapq.heapify(scoville)
#     while scoville:
#         if scoville[0]>=K:
#             return answer
#         n1=heapq.heappop(scoville)
        
#         if not scoville:
#             return -1
#         else:
#             n2=heapq.heappop(scoville)
#             heapq.heappush(scoville, n1+n2*2)
#             answer+=1
            
    #3차 풀이 100/100
    heapq.heapify(scoville)
    while scoville[0]<K:  
        if len(scoville)<2:
            return -1
        else:
            n1=heapq.heappop(scoville)
            n2=heapq.heappop(scoville)
            heapq.heappush(scoville, n1+n2*2)
            answer+=1

    return answer