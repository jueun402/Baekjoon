import sys
from collections import deque
# deque : 
# 링크드 리스트처럼 회전 가능, 왼쪽/오른쪽 삽입 삭제 가능 
# deque 모듈 rotate : 
# 인자가 음수일 경우 왼쪽으로 회전 , 양수가 주어지면 오른쪽 회전 

n, k = map(int,sys.stdin.readline().split())
dq = deque([i for i in range(1,n+1)]) 
result = [] # 제거된 사람들 list 

while dq:
    dq.rotate(-k+1)
    result.append(str(dq.popleft()))

sys.stdout.write("<"+", ".join(result)+">")

print("<"+", ".join(result)+">")