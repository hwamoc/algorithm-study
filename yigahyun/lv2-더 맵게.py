import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    # 리스트 최소 힙으로 만들기.
    for s in scoville:
        heapq.heappush(heap,s)

    while heap:
        if heap[0]>=K:
            return answer
        a = heapq.heappop(heap)
        if heap:
            b = heapq.heappop(heap)
            heapq.heappush(heap,a+b*2)
            answer += 1
    return -1


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))