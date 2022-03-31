## 백준 기초 1 
## 입출력 문제 모음 ## 

# 1. 1000번 (A+B)
A,B = map(int,input().split())
print(A+B)

# 2. 2558번 (A+B-2)
A = int(input())
B = int(input())
print(A+B)

# 3. 10950번 (A+B - 3)
while True:
    try:
        A,B = list(map(int,input().split()))
        print(A+B)
    except:
        break # EOF Error

# 4. 10951번 (A+B - 5)
while True:
    try:
        A,B = list(map(int,input().split()))
        if A+B == 0:
            break
        print(A+B)
    except: # EOF Error
        break

# 5. 10953번 (A+B - 6)

t = int(input())
for _ in range(t):
    A,B = map(int,input().split(","))
    print(A+B)


# 6. 11718번 11719번 (그대로 출력하기)

while True:
    try:
        str = input()
        print(str)
    except EOFError:
        break

# 7. 11719번 (그대로 출력하기)

N = int(input())
num = input()
print(sum(list(map(int,num))))


# 8. 11721번 (열 개씩 끊어 출력하기)

str = input()
for idx in range(0,len(str),10):
    print(str[idx:idx+10])

# 9. 2742번 (기찍 N)

n = int(input())
for i in range(n,0,-1):
    print(i)

# 10. 1924번 (2007년)

day = 0
MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS = ['SUN','MON','TUE','WED','THU','FRI','SAT']

x, y = map(int, input().split())

# x월 y일 
for i in range(x-1):
    day+=MONTHS[i] 
day = (day+y)%7

print(DAYS[day])

# 11. 2439번 (별 찍기 - 2)
n = int(input())
for i in range(n-1,-1,-1):
    print(' '*(i) + "*"*(n-i))

# 12. 2440번 (별 찍기 -3)
n = int(input())
for i in range(1, n+1):
    print("*"*(n-i+1))

# 13. 2442번 (별 찍기 - 5)
n = int(input())

for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))




  
# 4. 2193번 (이친수) -> dp
'''
0과 1로만 이루어진 수 = 이진수 
이친수 
- 0으로 시작 x 
- 1이 두 번 연속으로 나타나지 않는다. 11을 부분 문자열로 갖지 않는다. 
- N자리 이친수의 개수를 출력

규칙을 따라 이천수를 구해보면 패턴이 반복됨.
    1. N은 N-1의 결과에 + 0을 더한 것과 N-1의 결과에 01을 추가한 것과 동일함  
        - 자세한 내용은 https://pro-jy.tistory.com/15 참고
    2. N의 개수는 N-1의 결과와 N-2의 결과의 합과 동일함 => 피보나치 수열 
    3. 피보나치 개수 구하는 방식으로 N자리 이천수의 개수 출력  
'''
N = int(input()) 
result = [0 for _ in range(N+1)] 

for i in range(1,N+1):
    if i ==1 or i==2:
        result[i]=1
    else:
        result[i] = result[i-1]+result[i-2]
print(result[N])

# 5.  9465번 (스티커)
'''
단계별 최대값을 구하는 알고리즘
이렇게 숫자가 있다 가정했을 때, 
50	10	100	20	40
30	50	70	10	60

각 위, 아래 인덱스는 대각선의 값만 더할 수 있음 
분리해서 생각해보면 
50	10 
30	50
인덱스 1번 까지만 존재한다 가정,  10이 가질 수 있는 최대는 30
                                50이 가질 수 있는 최대는 50이다.
인덱스 2번 까지만 존재한다 가정,  100이 가질 수 있는 값은 (대각선 값)
                                1) 30   
                                2) 50 + 50
                                최대값은 2) 이므로 50+50을 선택 
                                70이 가질 수 있는 값은 
                                50, 10+30 중 MAX인 50이다.  
50	10+30	100	
30	50+50	70
인덱스 3번 까지만 존재한다 가정,  100이 가질 수 있는 값은 (대각선 값)
                                1) 30   
                                2) 50 + 50
                                최대값은 2) 이므로 50+50을 선택 
                                70이 가질 수 있는 값은 
                                50, 10+30 중 MAX인 50이다.  
50	10+30	100+50+50 20        20이 가질 수 있는 값 중 MAX = 70 + 50	
30	50+50	70+50	10          10이 가질 수 있는 값 중 MAX = 100+50+50 

인덱스 4번도 동일하게 반복 
50	10+30	100+50+50 20+70+50	40
30	50+50	70+50	10+100+50_50 60 

4번 반복 수행 결과

50	10+30	100+50+50 20+70+50	40+10+100+50+50
30	50+50	70+50	10+100+50+50 60+100+50+50

마지막 인덱스의 수행 내용은 모든 인덱스 값에서 가능한 선택지 중 최대값을 고려한 값
따라서 마지막 4번 인덱스에서 가장 큰 값을 선택한다. 
60+100+50+50 > 40+10+100+50+50 이므로 
최대값은 260이 된다 
    
참고 : https://pacific-ocean.tistory.com/197
'''
T = int(input())

for _ in range(T):
    s = []
    n = int(input())
    for _ in range(2):
        s.append(list(map(int,input().split())))

    s[0][1] += s[1][0]
    s[1][1] += s[0][0]

    for i in range(2,n):
        s[0][i] += max(s[1][i-1], s[1][i-2])
        s[1][i] += max(s[0][i-1], s[0][i-2])

    print(max(s[0][n-1], s[1][n-1]))
