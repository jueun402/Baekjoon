## BFS/DFS
[BFS/DFS 란? ](https://www.notion.so/playdatacademy/3-ce9db65d00e94d68be57342694701d45)

- 관련 내용
  - 프로그래머스
    - [타겟 넘버](https://programmers.co.kr/learn/courses/30/lessons/43165)
  - 백준 
    - [DFS와 BFS](https://www.acmicpc.net/problem/1260)
    - [바이러스](https://www.acmicpc.net/problem/2606)

---
### 깊이 우선 탐색?
- 하나의 경우의 수에 대해 모든 경우의 수를 조사하고 다음 경우의 수를 조사하며 해를 찾는 과정 
- 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없는 경우 다시 돌아와 다른 방향으로 다시 탐색 진행하는 방법과 유사하다. 

#### 깊이우선탐색(DFS)과 스택 
- EX 미로찾기 

```python

while len(stack)<0:
    now = stack.pop()
    if now == dest:
        return True
      
    x = now[1]
    y = now[0]
    
    if x -1 > -1:
      if maps[y][x-1] == 0:
          stack.append([y,x-1])














```
