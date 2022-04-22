# 연결 요소의 개수

# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

# 예제 입력 1 
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 예제 출력 1 
# 2
# 예제 입력 2 
# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3
# 예제 출력 2 
# 1


#---------------------------- 풀이 -----------------------------#


from collections import deque
import sys


def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    
    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i]= True


n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,sys.stdin.readline().split()) # input()-> sys로 바꿔야 시간초과 안 남 
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False]*(n+1)
result=0
for i in range(1,len(visited)):
    if visited[i] == False:
        result +=1
        bfs(graph,i,visited)

print(result)





#---------------------------- 풀이 2 (오류 - 시간초과) -----------------------------#

import sys

# 재귀 사용으로 인한 런타임 오류 발생
# 최대 재귀 횟수(1000회) 제한을 아래 메소드를 통해 풀어줌  
# 참고 : https://help.acmicpc.net/judge/rte/RecursionError
sys.setrecursionlimit(10**6)


n,m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,input().split())
    graph[u][v] = graph[v][u] = 1


def dfs(graph, v, visited):
    visited[v] = True
    # print(v,end=' ')
    
    for w in range(len(graph[v])):
        if graph[v][w] == 1 and visited[w] == False:
            dfs(graph,w,visited)

visited = [False]*(n+1)
result=0
for i in range(1,len(visited)):
    if visited[i] == False:
        result +=1
        dfs(graph,i,visited)

print(result)
