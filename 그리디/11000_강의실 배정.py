# 강의실 배정

# 문제
# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!

# 입력
# 첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

# 이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

# 출력
# 강의실의 개수를 출력하라.

#----------------------------------------------- 풀이 ---------------------------------------------------------#

# 풀이 생각
# 1. timetable을 si순서대로 정렬해놓는거지 
# 2. s1의 t1보다 s2가 작다 => 강의실 1개 추가 
# 3. 
# 
# s1 다음 s2가 작아 => 강의실 1개 추가 
# 3. 


# queue에 넣고 search..?

n = int(input())
timetable = []
for i in range(n):
    s, t = input().split()
    timetable.append([int(s),int(t)])

sorttime = sorted(timetable)

for i in range(len(sorttime)):
    print(i)

from collections import deque

queue = deque([])
queue.append(sorttime[0])

visited = [False]*len(sorttime)

def bfs(sorttime,v,visited):
    queue = deque([])
    visited[v] = True
    queue.append(sorttime[v])
            
    while queue:
        s1,t1 = queue.popleft()    
        
        v = 0
        for i in range(v+1,len(sorttime)):
            print(sorttime[i])
            s2, t2 = i
            if t1 <= s2:
                queue.append()
            print(s1,t1)
            
            
#######################################################

import heapq

n = int(input())

timetable = []

for i in range(n):
    s, t = map(int,input().split())
    timetable.append([s,t])

timetable.sort()

room = []
heapq.heappush(room,timetable[0][1])

sorttime = sorted(timetable)


graph = []

for i in range(len(sorttime)):
    
    
    
    
    