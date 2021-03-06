## 완전탐색/이분탐색
[완전탐색/이분탐색 이란? ](https://www.notion.so/2-1ff26adbd2b64f8da5525fcf797cefa0)

- 관련 내용
  - 프로그래머스
    - [모의고사](https://programmers.co.kr/learn/courses/30/lessons/42840)
    - [소수찾기](https://programmers.co.kr/learn/courses/30/lessons/42839)
  - 백준 
    - [숫자카드2](https://www.acmicpc.net/problem/10816)
---

### 01. 완전 탐색 
- 브루트포스 : 가능한 경우의 수를 탐색하여 효율성 관점에서 최악 
- 완전탐색 구현방법

1. 반복문

```python
def solution(trump):
    for i in range(len(trump)):
        if trump[i] == 8:
            return i
    
    return -1
```

2. 재귀함수 
    - 동적 계획법
    - 백트래킹
    - 탐욕법 

```python

def solution(trump, loc):
    if tump[loc]==8:
        return loc
    else:
        solution(trump,loc+1)

```

### 02. 이분 탐색 
- 오름차순으로 `정렬된 리스트`에서 특정 값의 위치를 찾는 알고리즘 
- 중간값을 선택하여 찾고자 하는 값과 크고 작음을 비교하는 방법 
- left, right, mid값으로 알고리즘이 구성되어있음 

ex. updown 게임 
    1~1000 => 기회는 8번 
    500 up
    750 
    ...

```python
def solution(trump):
    # 함수 시작시 left, right를 선언 
    left = 0
    right = len(trump)-1

    # left가 right보다 작거나 같다면 
    while (left <= right):
        mid = (left + right) //2 # mid값 계산 

        if trump[mid] == 8:
            return mid # 정답을 찾으면 반환 
        
        # 정답보다 작다면 left를 mid+1로 올려주어 계산
        elif trump[mid] < 8:
            left = mid+1

        # 정답보다 크다면, right를 mid-1로 내려주어 계산 
        elif trump[mid] > 8:
            right = mid-1
    return mid 


```
