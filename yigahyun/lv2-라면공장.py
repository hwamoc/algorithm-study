import heapq as hq

def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    idx = 0
    while stock < k:
        for i in range(idx, len(dates)):
            if stock >= dates[i]: # 재고가 4이면 3일까지는 괜찮음.
                hq.heappush(heap, (-supplies[i], supplies[i]))
                idx += 1
            else: # 재고가 4이면 4일째는 공급 받아야 함.
                break
        stock += hq.heappop(heap)[1]
        answer += 1
    return answer

print(solution(4, [4, 10, 15, 25], [20, 5, 10, 20], 30))
