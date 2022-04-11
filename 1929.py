# 소수 구하기

# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 예제 입력 1 
# 3 16
# 예제 출력 1 
# 3
# 5
# 7
# 11
# 13

#--------------------------풀이--------------------------------#

## 시간 초과 
m, n = map(int,input().split())

for i in range(m,n+1):
    condition = True
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                condition=False
                break
        if condition:
            print(i) 

 
# 에라스토네의 체 사용 
# 1을 제거 => 지워지지 않는 수 중 제일 작은 2를 소수로 선택 => 2의 배수를 모두 지움 
# 지워지지 않는 수 중 제일 작은 3을 소수로 선택 -> 나머지 3의 배수를 모두 지움 ... 

m, n = map(int,input().split())

for i in range(m,n+1):
    condition = True
    if i > 1:
        # n의 제곱근 까지만 검사 
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                condition=False
                break
        if condition:
            print(i) 

