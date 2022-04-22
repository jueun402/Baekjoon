# https://www.acmicpc.net/problem/11057
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-11057-%EC%98%A4%EB%A5%B4%EB%A7%89-%EC%88%98#%EC%A0%90%ED%99%94%EC%8B%9D

n = int(input())

dp = [[0]*10 for _ in range(n+1)]
dp[1] = [1,1,1,1,1,1,1,1,1,1]

for i in range(2,n+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])
      
print(sum(dp[n])%10007)