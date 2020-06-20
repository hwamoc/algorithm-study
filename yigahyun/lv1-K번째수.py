import heapq
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1] - 1
        k = commands[i][2]
        heap = []
        for j in range(start,end+1):
            heapq.heappush(heap, array[j]) # 최소힙 만들기
        for _ in range(k):
            kth_min = heapq.heappop(heap) # k번 째 최소 값 찾기
        answer.append(kth_min)
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))