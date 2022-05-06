

# 01. 한 개의 회의실
# 02. N개의 회의에 대해 회의실 사용표
# 03. 회의에 대해 시작시간 - 끝나는 시간 표 O 
# 04. 겹치지 않게 하면서, 회의실을 사용할 수 있는 회의의 최대 개수 
# 05. 회의는 한번 시작하면 중간에 중단될 수 없으며 회의가 끝나는 것과 동시에 다음 회의 시작 가능 

import heapq

n = int(input()) 
schedule = []
for i in range(n):
    start, end = map(int,input().split())
    schedule.append([start,end])

# 회의 시작 시간 기준으로 정렬 
schedule.sort(key=lambda x : x[0])

# 회의 
queue= []
heapq.heappush(queue, schedule[0])

s,t = queue[0]

for i in range(1,len(schedule)):
    # 현재 회의 종료 시간 <= 다음 회의 시작 시간 
    if t <= schedule[i][0]:
        
        
        
        
        