# DFS와 BFS 

# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1 
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 예제 출력 1 
# 1 2 4 3
# 1 2 3 4
# 예제 입력 2 
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1
# 예제 출력 2 
# 3 1 2 5 4
# 3 1 4 2 5
# 예제 입력 3 
# 1000 1 1000
# 999 1000
# 예제 출력 3 
# 1000 999
# 1000 999


#----------------------------방법 1 (인접 행렬 방식) ------------------------------#

import sys
from collections import deque

# 너비 우선 탐색 
def bfs(graph, start, visited):

    # 큐 구현 위해 deque 사용 
    queue = deque([start])
    
    # 현재 노드 방문 처리 
    visited[start] = True

    # queue가 빌 때 까지 반복 
    while queue:
        # queue에서 하나의 원소 뽑아 출력 
        v = queue.popleft()
        print(v,end=' ')

        # 원소에 연결된 방문하지 않은 원소들 삽입 
        for w in range(len(graph[v])):
            if graph[v][w] == 1 and visited[w] == False:
                queue.append(w)
                visited[w] = True


def dfs(graph,v,visited):
    visited[v] = True

    print(v,end=' ')
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and visited[i]==False:
            dfs(graph,i,visited)



# 정점 개수, 간선 개수, 탐색 시작 정점 번호
n, m, v = map(int,input().split())

visited = [False]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    i, j = map(int,sys.stdin.readline().split(' '))
    graph[i][j] = graph[j][i] = 1


dfs(graph,v,visited)
visited = [False]*(n+1)
print()
bfs(graph,v,visited)


#----------------------------방법 2 (인접 리스트 방식) ------------------------------#


import sys
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])

    # 현재 노드 방문 처리 
    visited[start] = True

    # 큐가 빌 때 까지 반복 
    while queue:    
        # 큐에서 하나의 원소 뽑아 출력 
        v = queue.popleft()
        print(v, end=' ')

        # 원소와 연결된 방문하지 않은 원소들 queue에 삽입 
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                # 원소 방문 처리 
                visited[i] = True
    
def dfs(graph,v,visited):
    
    visited[v] = True
    print(v,end=' ')

    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph,i,visited)


# 정점 개수, 간선 개수, 탐색 시작 정점 번호
n, m, v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)



dfs(graph,v,visited)
visited = [False]*(n+1)
print()
bfs(graph,v,visited)

