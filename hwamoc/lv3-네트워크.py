def dfs(computers, visited, v):
    if visited[v] == 0:
        visited[v] = 1      # 방문했음을 표시
    for e in range(len(computers)):
        if computers[v][e] == 1 and visited[e] == 0:    # 인접 노드이고, 방문된 적이 없는 경우
            dfs(computers, visited, e)

def solution(n, computers):
    visited = [0] * n   # 방문한 노드를 체크해 둘 리스트
    answer = 0          # 네트워크의 개수를 저장할 변수
    while 0 in visited:         # visited 리스트의 모든 값에 방문 표시가 되어있을 때까지 반복
        for i in range(n):
            if visited[i] == 0:
                dfs(computers, visited, i)
                answer += 1     # 한 네트워크의 탐색을 마치면 개수 추가
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))