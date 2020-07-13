from collections import deque

def solution(priorities, location):
    
    priorities = [(x, priorities[x]) for x in range(len(priorities))]
    Q = deque(priorities)
    
    cnt = 0
    while len(Q) > 1:
        x = Q.popleft()
        #print(x)
        if x[1] >= max([x[1] for x in Q]):
            #print(x)
            cnt +=1
            if x[0] ==location:
                return cnt
        else:
            Q.append(x)
    return cnt+1










def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer