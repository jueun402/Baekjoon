# 풀이 1 Counter 함수 사용 
from collections import Counter

cardNum = int(input())
card = list(map(int, input().split()))
M = int(input())
card_to_find = list(map(int, input().split()))

card.sort()

cntCard = Counter(card) 
for i in card_to_find:
    print(cntCard[i],end=" ")


#-----------------------------------------------------------------#

# 풀이 2. 이분탐색 활용 

# 상근이가 갖고있는 숫자
N = int(input())
card = list(map(int,input().split()))

# 정수 M개
M = int(input())
ary = list(map(int,input().split()))

# 정렬 
card.sort()

# card에 정수 M이 있는지 확인 
def binary_search(target, card):
    start, end = 0,len(card)-1
    cnt = 0

    while start <= end:

        mid = (start+end)//2
        if card[mid] == target:
            # target이 존재하면 start - end 범위 card에 존재하는 target count 
            return card[start:end+1].count(target)

        elif card[mid] < target:
            start = mid+1
        else:
            end = mid-1

    # 찾지 못하면 return 0
    return 0

# ary에 있는 애를 target으로 하고 
for target in ary:
    print(binary_search(target,card), end=' ')
        
# card를 count하는 부분에서 시간초과가 났다
# start와 end의 범위 만 탐색해 count해서 해결했따.
# https://chancoding.tistory.com/45 
# 이 분의 해설을 보니 이분탐색 보다 위에 counter 함수를 사용한게 메모리나 시간이 더 적었다.
# hash를 사용한 방법도 고안해보자 