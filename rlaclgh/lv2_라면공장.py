
import heapq as hq
def solution(stock, dates, supplies, k):
    stock_heap = []
    for i in range(len(dates)):
        hq.heappush(stock_heap,(dates[i],supplies[i]))
    cnt = 0
    selected_heap = []
    while True:
        if stock >=  k:
            break
        while True:
            if len(stock_heap) !=0 and stock >= stock_heap[0][0]:
                i , j = hq.heappop(stock_heap)
                hq.heappush(selected_heap,(-j,i))
            else:
                break
        i , j = hq.heappop(selected_heap)
        stock += (-i)
        cnt += 1
    return cnt