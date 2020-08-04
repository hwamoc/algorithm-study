def solution(n, edge):
  graph = [[] for _ in range(n + 1)]
  distances = [0 for _ in range(n)]
  is_visit = [False for _ in range(n)]
  queue = [0]
  is_visit[0] = True
  for (a, b) in edge:
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

  while queue:
    i = queue.pop(0)

    for j in graph[i]:
      if is_visit[j] == False:
        is_visit[j] = True
        queue.append(j)
        distances[j] = distances[i] + 1

  distances.sort(reverse=True)
  answer = distances.count(distances[0])

  return answer

'''
from collections import defaultdict


def bfs(graph, start, distances):
    q = [start]
    visited = set([start])

    while len(q) > 0:
        current = q.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                distances[neighbor] = distances[current] + 1

def solution(n, edge):
    # 그래프 만들기
    graph = defaultdict(list)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # bfs 탐색 (최단 거리를 구해야 하므로.)
    distances = [0]*(n+1)
    bfs(graph, 1, distances)

    max_distance = max(distances)
    answer = 0

    for distance in distances:
        if distance == max_distance:
            answer += 1

    return answer
'''
'''
def solution(n, edge):
    answer = 0
    node = {i:-1 for i in range(1, n+1)}

    # update graph
    graph = {i:list() for i in range(1, n+1)}
    node[1] = 0
    for e in edge:
        st = e[0]
        ed = e[1]
        graph[st].append(ed)
        graph[ed].append(st)

    updated_node = [1]
    next_updated_node = []
    def update_graph(num, node_num):
        """
        num: 거리
        node: 현재 update된 node
        """
        next_updated_nodes = []
        next_node_list = graph[node_num]

        for next_node in next_node_list:
            if node[next_node] == -1:
                node[next_node] = num
                next_updated_nodes.append(next_node)
        return next_updated_nodes

    for i in range(1, n+1):
        for up in updated_node:
            next_updated_node += update_graph(i, up)
        updated_node = next_updated_node[:]
        next_updated_node = []

        if len(updated_node) == 0:

            res = len(list(filter(lambda x: node[x] == i-1, node.keys())))
            break
    return res
'''
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))