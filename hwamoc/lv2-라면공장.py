import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    sup_heap = []
    start = 0

    while stock < k:
        for i in range(start, len(dates)):
            if dates[i] <= stock:
                # print("date", i, dates[i], "stock", stock)
                heapq.heappush(sup_heap, -supplies[i])
                # print(sup_heap)
                start = i + 1
            else:
                break
        stock += -heapq.heappop(sup_heap)
        answer += 1

    return answer

solution(4, [4, 10, 15], [20, 5, 10], 30)
