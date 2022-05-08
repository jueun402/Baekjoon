# 트리의 부모 찾기

# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

# 예제 입력 1 
# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7

# 예제 출력 1 
# 4
# 6
# 1
# 3
# 1
# 4

import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 늘려주기 

def dfs(graph,v,visited):
    
    visited[v] = True
    # print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:
            result[i]= v
            dfs(graph,i,visited)

n = int(input())

graph = [[] for _ in range(n+1)]
visited=[False]*(n+1)
result = {} # 딕셔너리 활용 

# 그래프 노드 입력 받기 
for _ in range(n-1):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v) 
    graph[v].append(u)

dfs(graph, 1, visited)

for i in range(2,n+1):
    print(result[i])



import sys

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = {}

for i in range(n-1):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, v ,visited):
    visited [v]=True # 방문 처리 
    print(v,end='')
    
    for i in graph[v]:
        #  방문하지 않았다면 
        if not visited[i]: 
            result[i] = v  # i노드의 부모는 v 
            dfs(graph,i,visited)
