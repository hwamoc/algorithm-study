import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            print(scoville, scoville[0])
        except IndexError:
            return -1
        answer += 1
        print(answer)

    return answer

solution([1, 2, 3, 9, 10, 12], 7)
solution([1, 2, 3, 4, 5, 6], 80)