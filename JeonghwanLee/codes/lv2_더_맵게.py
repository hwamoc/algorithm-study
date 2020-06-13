import heapq

def check_over(scoville, K): #0번쨰 인덱스가 K보다 큰지 비교하는 함수
    if scoville[0]>K:
        return True
    else:
        return False


def solution(scoville, K):
    count = 0#섞은 count
    heapq.heapify(scoville) #min힙 생성
    while(not check_over(scoville, K)): #min힙의 root가 K보다 크지 않다면 
            min_1 = heapq.heappop(scoville)#2개 pop해서섞어서 넣음
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville,min_1+min_2*2)
            count+=1
            
            if len(scoville) is 1: #다 스까쓸떄
                if scoville[0]<K:
                    return -1
                else:
                    return count
        
    return count