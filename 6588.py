# 골드바흐의 추측 다국어

# 문제
# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

# 이 추측은 아직도 해결되지 않은 문제이다.

# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

# 입력
# 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.

# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)

# 입력의 마지막 줄에는 0이 하나 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다. 만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

# 예제 입력 1 
# 8
# 20
# 42
# 0
# 예제 출력 1 
# 8 = 3 + 5
# 20 = 3 + 17
# 42 = 5 + 37


#--------------------------풀이 1 --------------------------------#

## 1. n까지 소수 list를 생성해서 
## i도 소수 && n-i도 소수일 경우 출력

## 결과 : 시간초과 
import sys

def isPrime(n):
    prime = []
    for i in range(2,n):
        condition = True
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                condition = False
                break
        if condition:
            if i%2 !=0:
                prime.append(i)
    return prime


while True:
    n = int(sys.stdin.readline())
    condition = False
    pLists = isPrime(n) # 2~n까지의 prime List

    if n == 0:
        break

    for i in pLists:
        # 만약 (n- 소수) == '소수' 라면  
        if n-i in pLists:
            print(str(i)+' + '+str(n-i))
            condition = True
            break

        if i >= n:
            condition=False
            break

    # 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우 
    if not condition:
        print("Goldbach's conjecture is wrong.")

#--------------------------풀이 2 --------------------------------#
# 이렇게도 에라토스테네스 체를 풀 수 있다! 
n = 10
array = [True for i in range(n+1)]

for i in range(2, int(n**0.5)+1):
    if array[i]:
        for k in range(i + i, n+1, i):
            print(i,k)
            array[k] = False

# 맞았다!

import sys

def isPrime():
    array = [True for i in range(10000001)]
    # (1000000**0.5)+1 == 1001
    for i in range(2,1001):
        if array[i]:
            for j in range(i+i, 10000001, i):
                array[j] = False
        
    return array

pLists = isPrime() # 2~n까지의 prime List

while True:
    n = int(sys.stdin.readline())
    condition = False
    if n == 0:
        break

    for i in range(3,len(pLists)):
        if pLists[i] and pLists[n-i]:
            condition=True
            print(str(n) +" = " +str(i)+' + '+str(n-i))
            break

    # 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우 
    if not condition:
        print("Goldbach's conjecture is wrong.")