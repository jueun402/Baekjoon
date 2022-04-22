# 계단 오르기 규칙 

# 1. 한번에 한 계단 or 두 계단씩 오를 수 있음 
#     한 계단 밟으면서 이어서 다음 계단이나 다음 다음 계단으로 오를 수 있다 
#     1+1
#     1+2

#     1+1+1 (x)
#     1+1+2 (o)
#     2+1+1

# 2. 연속된 세 개의 계단을 모두 밟으면 안된다.
# 3. 마지막 도착 계단은 무조건 밟아야 함 

# - 점수의 최댓값을 구하라 

# n = int(input())
# floor=[]
# for _ in range(n):
#     floor.append(int(input()))

# 경우의 수 
#     끝 계단 = floor[5]
#     1) floor[4] -> floor[5]
#     2) floor[3] -> floor[5]



# 가능한 패턴 
# 1121
# 212
# 221
# 122

# 최대값 = [10,20,25,10,20]


# floor 0은 시작 지점 
# floor = [0, 10, 20, 15, 25, 10, 20]

# 15에서 가능한 경우 
# 1) 10 + 15 = floor[3-2]+floor[3]
# 2) 0 + 20 + 15 = floor[3-1]+floor[3-3]+floor[3] 이다. 

# 여기서 max값은 2)의 경우인 35가 된다. 





# n = int(input())
# floor=[]
# for _ in range(n):
#     floor.append(int(input()))


# 패턴은 뒤에서부터 

# [10, 20, 15, 25, 10, 20]
#         1 <- 2 <- 2
#         2 <- 1 <- 2
#         1 <- 2 <- 1
#         2 <- 2 <- 1


#         = 1과 1은 연속적으로 나올 수 없음 
#         = 2는 연속으로 나와도 상관 x 
#         = 따라서, 1로 시작하면 

#         1212

#         - 이거 조건만 고려하면 되겠다. 
#             1로가서 2로가는게 좋은지, 2로가는게 좋은지 


n = int(input())
floor=[]
for _ in range(n):
    floor.append(int(input()))



rev_floor = floor[::-1]
dp = floor.copy()


max(floor[i+1]+floor[i+3], floor[i+2]) => 이거 구해서 dp에 넣으면 됨 


for i in range(n):
    # max(1로 시작, 2로 시작)
    if max(floor)
    



패턴을 뒤에서부터  파악>

[10, 20, 15, 25, 10, 20]
        1 <- 2 <- 2
        2 <- 1 <- 2
        1 <- 2 <- 1
        2 <- 2 <- 1

        = 1과 1은 연속적으로 나올 수 없음 
        = 2는 연속으로 나와도 상관 x 

        - 따라서 

        max(floor[i-1]+floor[i-3], floor[i-2]) => 이거를 구해서 dp에 넣으면 된다.


* 점화식은 찾았는데 dp에 적용하는 방법이 어려워 다른 코드들을 참고했다.


[10, 20, 15, 25, 10, 20]

dp는 반복적으로 계산되는 값을 저장해두는 저장소이다.

i = 0부터 시작한다고 가정해보면, seq[i]에서의 max값을 dp에 저장해두어야 한다.

i가 0, 1, 2일 때, 가능한 경우는 한 가지이다. 

seq[0]의 max값은 자기 자신이다. dp[0] = seq[0] 
seq[1]의 max값은 seq[0]과 seq[1]을 더한 값이다. dp[1] = seq[0] +seq[1]
seq[2]의 max값은 3개의 계단을 연속으로 밟을 수 없으므로 seq[0]과 seq[2]를 더한 값이다. dp[2] = seqp[0] + seq[2]

[10, 20, 15, 25, 10, 20]

seq[3]은 max(seq[3]+seq[2] + seq[0], seq[1]+seq[3])이다. 






    
    
    (rev_floor[i+1]+rev_floor[i+3]) > rev_floor[i+2]:
        dp[i] = rev_floor[i+1]+rev_floor[i+3]
        i = i+3
     

    dp[i] = max(rev_floor[i]+)





######## 14. 시저 암호 ########
## ex. "AB"는 1만큼 밀면 "BC", 3만큼 밀면 "DE"
## ex. "z"는 1만큼 밀면 "a"

def solution(s, n):

    a = list(range(97,123)) # a~z
    A = list(range(65,91)) # A~Z 

    s = list(s)

    for i in range(len(s)):
        if s[i] ==" ":
            continue
        
        if s[i].isupper(): # 대문자 
            s[i] = chr(A[int(((ord(s[i])+n) - 65) % 26)])
        
        else:
            s[i] = chr(a[int(((ord(s[i])+n) - 97) % 26)])

    answer = ""
    for i in s:
        answer +=i 

    return answer   


    