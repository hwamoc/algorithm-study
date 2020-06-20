import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    rev_supplies = list(map(lambda x:-x, supplies)) #max heap을 만들기 위해 전체에 마이너스 취함
    dates.append(k) #마지막날 추가
    supplies.append(0)
    
    heap = []
    temp_index = 0 #마지막으로 힙을 push했던 위치
    
    for i,date in enumerate(dates):        
        
        if stock<date:  #이날까지 못갈 것 같다면
            local_supplies = rev_supplies[temp_index:i] #전까지의 부분집합으로 힙 만들것
            
            for supply in local_supplies:     #전 date까지 heap push
                heapq.heappush(heap,supply) 
            
            while stock<date: #오늘 버틸 보급품이 있을때까지    
                answer+= 1
                popped = heapq.heappop(heap)
                stock-= popped   #마이너스 취했으니 뺴줌
            
            temp_index = i
    return answer