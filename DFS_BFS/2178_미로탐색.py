
# 미로 탐색 성공

# 문제
# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.


from collections import deque

n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]

 
def bfs():

    # 초기 좌표 
    x,y = 0,0
    queue = deque([])
    queue.append([x,y])
    
    dx, dy = [-1,1,0,0], [0,0,-1,1]

    maze[0][0] = 2 # 0,0이 1이면 계속 더해짐 
    
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y

            if 0<=nx<m and 0<=ny<n and maze[ny][nx]==1:
                maze[ny][nx] = maze[y][x]+1
                queue.append([ny,nx])

bfs()

# 0,0에 1을 더해줬으니 마지막에 빼줌 
print(maze[n-1][m-1]-1)