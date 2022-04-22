import sys
from collections import deque

def bfs(graph, v ,visited):
    visited[v] = True
    queue = deque([v])

    while queue:
        v = queue.popleft()
        # print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())
    lists = [0]+list(map(int,sys.stdin.readline().split()))
    visited = [False]*(n+1)
    result = 0

    graph = [[] for _ in range(n+1)] 
    
    for i in range(1,n+1):    
        graph[i].append(lists[i])
        graph[lists[i]].append(i)

    for i in range(1,n+1):
        if not visited[i]:
            dfs(graph,i,visited)
            result +=1

    print(result)


## 시간초과 
## 아래와 같이 하면 시간초과 난다..


# import sys
# from collections import deque

# def bfs(graph, v ,visited):
#     visited[v] = True
#     queue = deque([v])

#     while queue:
#         v = queue.popleft()
#         # print(v,end=' ')
#         for i in range(len(graph[v])):
#             if graph[v][i] == 1 and not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


# t = int(input())

# for _ in range(t):
#     n = int(sys.stdin.readline())
#     lists = [0]+list(map(int,sys.stdin.readline().split()))
#     visited = [False]*(n+1)
#     result = 0

#     graph = [[0]*(n+1) for _ in range(n+1)] 
    
#     for i in range(1,n+1):    
#         graph[i][lists[i]] = 1
#         graph[lists[i]][i] = 1    

#     for i in range(1,n+1):
#         if not visited[i]:
#             bfs(graph,i,visited)
#             result +=1

#     print(result)
