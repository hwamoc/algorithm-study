import heapq as hq

def solution(scoville, K):
    a = []
    for i in scoville:
        hq.heappush(a,i)
    cnt = 0
    while True:
        if a[0] >= K:
            break
        elif len(a) ==1:
            return -1
        else:
            hq.heappush(a,hq.heappop(a)+hq.heappop(a)*2)
            cnt +=1
    return cnt