nums = [2,7,11,15]
target = 9


def twoSum(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if( nums[i] + nums[j] == target):
                return[i,j]

# 시간복잡도 : O(N^2)
# 공간복잡도 : O(1) -> 새로운 변수를 사용하는것이 없음 


def twoSum2(nums,target):
    for i, num in enumerate(nums): # for문 O(N)
        res = target-num
        if res in nums[i+1::]: # 검색 => O(N)
            return [i, i+1+nums[i+1::].index(res)] # index 시간복잡도 = O(N)

# 시간복잡도  : O(N^2)
# O(N) (O(N) + O(N)) = 2*O(N^2) == O(N^2)


# 해시테이블 사용 !! 
def twoSum3(nums,target):
    dicts = {}
    # nums를 한번 순회해야 함
    for i, num in enumerate(nums): # for문 O(N)
        res = target - num
        if res in dicts: # res값이 dictionary에 key값으로 존재한다면  O(1)
            return [i, dicts[res]] # O(1)
        # key, value 값으로 저장 
        dicts[num]=i # index값을 저장 


        
        
# 시간복잡도 : O(N)

# 어떤 자료구조를 사용해서 어떻게 해결 할 것인가? 
# dictionary 



## 스택을 queue처럼 동작하게 함
# pop했을 때 마지막에 있는 element가 나옴 
# queue처럼 동작하게 하기 위해 pop(0) index를 넣어줌 
# 문제 => 시간 복잡도 
# 배열에서 0번째 인덱스를 제거했을 때 시간복잡도? 
# O(1)이 걸림 
# 0번째 index를 제거하는데 걸리는 시간은 O(N)
# 0번째 index를 뺌 => index가 사라지면 채워줘야 함 
# 전부 다 왼쪽으로 shift 되는 일이 발생 
#  

def solution(bridge_length, weight, truck_weights):
    # 1. 마지막 트럭을 제외한 모든 트럭이 다리를 통과하는데 걸리는 시간 
    time = 0

    # 2. 현재 다리의 트럭 무게 총합 
    total_weight = 0

    # 3. 다리 -> 큐 
    bridge = [0]*bridge_length

    while(len(truck_weights)>0): # 0(N)
        tmp = bridge.pop(0) # bridge의 맨 앞 값 # O(N)
        total_weight -= tmp # 다리를 빠져나감과 동시에 total_weight를 빠져나감 

        # 현재 다리의 트럭 무게 총합 + 대기 1번 트럭의 무게 > weight 
        if total_weight + truck_weights[0] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop(0) # 0번째 index의 element pop 
            bridge.append(truck)
            total_weight += truck
        
        time +=1
    
    # 마지막 트럭이 올라간 상태 + 다리의 길이를 더해주면, 모든 트럭이 통과하는데 
    # 걸리는 시간 
    return time  + bridge_length

# 시간복잡도 : O(N^2)


# 양 끝에서 동시에 삽입/삭제 가능한 자료구조 

# Linked List를 이용해 구현된 자료구조 
from collections import deque
from copy import deepcopy
import enum 

def solution(bridge_length, weight, truck_weights):
    time = 0
    total_weight = 0
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights.reverse() # 마지막 index의 값을 pop하겠다 (truck_weights는 list 값이므로)

    while(truck_weights): 
        tmp = bridge.popleft()
        total_weight -= tmp 
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop() # 대기 1번 index의 element pop 
            bridge.append(truck)
            total_weight += truck
        time +=1

    return time  + bridge_length

# 시간 복잡도 : O(1)

# 모든 가능한 케이스에 대해서 시뮬레이션 
from itertools import combinations_with_replacement

def solution(n, info): # 화살 개수, 어피치 과녁 정보 
    # 가장 큰 점수차로 이길 수 있는 과녁 정보를 담은 배열 
    answer = [0 for _ in range(11)]
    win = False # 마지막에 라이언이 이길 경우 True, False라면 라이언 lose  
    max_score =  0 # 라이언이 이길 때 가장 큰 점수 차이 

    # 1. 중복조합을 이용해 라이언의 점수 만들기 
    for res in list(combinations_with_replacement(range(11), n)): # 화살종류, 몇 개를 뽑아야 할지 
        now = [0 for _ in range(11)] # 과녁 정보를 담을 배열
        # 리스트 안에 res라는 정보는 5발을 쐈다면 => 0~10까지 10,10,10,9 9 이런식으로 
        # 원하는 형태가 아님 => 10점이 3발이면 0번째 인덱스에 3, 9점을 두발 쐈으면 1번째 인덱스에 2 
        for r in res:
            now[10-r] += 1

        lion, apeach = 0, 0

        # 2. 라이언, 어피치 점수 비교 
        for i, (l, p) in enumerate(zip(now,info)):
            if l == p == 0: # 0개를 쐈다면 
                continue
            if p >= l : # 어피치가 라이언보다 높은 점수
                apeach += (10-i) 
            elif l > p:
                lion += (10-i) 
        
        # 3. 총 점수 비교해서 라이언이 큰 경우 결과 업데이트 
        if lion > apeach : 
            win = True
            if (lion - apeach) > max_score:
                max_score = lion- apeach
                answer = now

    # 라이언이 졌다면             
    if not win:
        return [-1]    

    return answer 
    
         

# 완전 탐색 방법 

# 최대 점수, 최대 점수 배열 
max_score, max_board = 0, [] # 전역으로 선언 
def solution(n, info): 

    def dfs(ascore, lscore, cnt, idx, board): # apeach score, lion score, 화살 쏜 개수, 점수
        global max_score, max_board
        # 언제 재귀함수 탈출 할 것인지 알려줘야 함 
        
        if cnt > n: # n은 문제에서 주어진 화살 개수 
            return 
        
        if idx > 10: # index 하나씩 증가 
            diff = lscore - ascore 
            if diff > max_score:
                board[10] = n - cnt
                max_score = diff
                max_board = board
            return 

        if cnt < n:
            cboard = deepcopy(board)
            cboard[10-idx] = info[10-idx]+1
            dfs(ascore, lscore+idx, cnt+info[10-idx]+1, idx+1, cboard)

        
        ccboard = deepcopy(board)
        if info[10-idx] > 0: # apeach가 이기게 되는 상황 
            dfs(ascore+idx, lscore, cnt, idx+1, ccboard) 
        else:
            dfs(ascore, lscore, cnt, idx+1, ccboard)

    dfs(0, 0, 0, 0, [0]*11)
    if max_board:
        return max_board
    else:
        return [-1]



















