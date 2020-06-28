cnt = 0
def DFS(n,res,numbers,target):
    global cnt
    if n == len(numbers):
        if res == target:
            cnt +=1
            return
    else:
        DFS(n+1,res+numbers[n],numbers,target)
        DFS(n+1,res-numbers[n],numbers,target)

def solution(numbers, target):
    global cnt
    DFS(0,0,numbers,target)
    return cnt