# 문제 : https://www.acmicpc.net/problem/2011
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-2011-%EC%95%94%ED%98%B8%EC%BD%94%EB%93%9C

n = input()
dp = [0 for _ in range(len(n)+1)]

# 암호가 0으로 시작한다면 아예 해독이 불가능하다 
if n[0] == '0':
    print('0')

# 암호가 0으로 시작하지 않는 경우      
else:    
    # dp[0], dp[1] 은 항상 1이다. 
    dp[0] = 1 
    dp[1] = 1
    n = '0'+n
    for i in range(2,len(n)):
        # case [a] : i번째 숫자가 단독으로 존재하는 경우 
        if n[i] > '0':
            dp[i] += dp[i-1]
        # case [b] : i번째 숫자가 결합해서 존재하는 경우
        if n[i-1] != '0' and n[i-1] + n[i] < '27':
            dp[i] += dp[i-2]

    print(dp[len(n)-1]%1000000)

