# 트리의 지름

# 문제
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

# 입력
# 트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

# 먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

# 출력
# 첫째 줄에 트리의 지름을 출력한다.

# 예제 입력 1 
# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1
# 예제 출력 1 
# 11

#------------------------------풀이-----------------------------#
# 트리의 지름에 대한 자세한 내용은  https://bedamino.tistory.com/15 여기서 보자 


import sys
from collections import deque
sys.setrecursionlimit(10**9)

V = int(input())
graph = [[] for _ in range(V+1)]


for _ in range(V):
    ary = list(map(int,sys.stdin.readline().split()))
    # [정점] 정점1, 거리, 정점2, 거리 ... 간격으로 트리 저장 
    for i in range(1,len(ary)-2,2):
        graph[ary[0]].append([ary[i], ary[i+1]])

def bfs(v):
    queue = deque([])
    queue.append(v)

    while queue:
        t = queue.popleft()
        for a,b in graph[t]:
            if distance[a] == -1:
                distance[a] = distance[t]+b
                queue.append(a)

                
def dfs(v,dist):

    for i in graph[v]:
        a,b = i # 다음 좌표 , 길이 

        # 방문하지 않은 노드라면 
        if distance[a] == -1: 
            # a까지 도달하는 거리 = a에 도달하기 전 거리 + a까지 도달하는 거리
            distance[a] =  dist+b  
            dfs(a,dist+b)

    
# 임의의 노드(1) 에서 가장 먼 노드(a) 찾기
distance = [-1]*(V+1) # 노드까지의 길이 저장
distance[1] = 0 # root노드 길이 0으로 초기화 
# dfs(1,0)
bfs(1)

# 가장 먼 노드(a)에서 가장 먼 노드(b) 찾기 
A = distance.index(max(distance))
distance = [-1]*(V+1)
distance[A] = 0
# dfs(A,0)
bfs(A)

print(max(distance))



# 참고 
# https://kyun2da.github.io/2021/05/04/tree's_diameter/

# 후기 
# 트리의 지름을 찾는 알고리즘을 공부했다! 
# bfs dfs를 두번 쓰는 문제 어렵다 ㅠ 
# dfs로 풀어봤으니 bfs로 풀어봐야겠다. (맞았다!)
