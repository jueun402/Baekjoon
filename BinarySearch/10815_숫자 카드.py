# 숫자 카드

# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

#--------------------------------풀이-------------------------------------
# 역시 시간초과

# 상근이가 갖고있는 숫자
N = int(input())
card = list(map(int,input().split()))

# 정수 M개
M = int(input())
ary = list(map(int,input().split()))

result = ['0']*M

for i in card:
    try:
        result[ary.index(i)] = '1'
    except:
        continue

print(" ".join(result))

#--------------------------------풀이-------------------------------------
# 정답!! 

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
    
    while start <= end:

        mid = (start+end)//2
        if card[mid] == target:
            return 1
        elif card[mid] < target:
            start = mid+1
        else:
            end = mid-1

    # 찾지 못하면 return 0
    return 0

# ary에 있는 애를 target으로 하고 
for target in ary:
    print(binary_search(target,card), end=' ')
        