# 이분 그래프

# 문제
# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

# 그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 

# 출력
# K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

# 제한
# 2 ≤ K ≤ 5
# 1 ≤ V ≤ 20,000
# 1 ≤ E ≤ 200,000
# 예제 입력 1 
# 2
# 3 2
# 1 3
# 2 3
# 4 4
# 1 2
# 2 3
# 3 4
# 4 2
# 예제 출력 1 
# YES
# NO

#---------------------------- 풀이 -----------------------------#

import sys
from collections import deque

def bfs(graph,v,visited):
    queue = deque([v])
    visited[v] = 1  # 정점 1일때 1로 초기화 
    while queue:
        v = queue.popleft()

        for i in sorted(graph[v]):
            # 정점을 방문하지 않았을 경우 
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v]*-1 # v 정점과 반대되는 색으로 칠하기
            
            # 이미 정점에 방문한 경우 
            elif visited[i]*visited[v] > 0: # 동일한 색이라면 
                return 0 # RETURN 0
                
    return 1 # 동일한 색이 걸리지 않으면 RETURN 1 

k = int(input())

for _ in range(k):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    result = 0    
    
    # 그래프 생성 
    for i in range(E):
        u, v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # BFS - 노드가 끊어진 경우 고려 
    for i in range(1,len(visited)):
        if not visited[i]:
            result = bfs(graph,i,visited)
        if not result:
            break
    
    print("YES" if result else "NO") 