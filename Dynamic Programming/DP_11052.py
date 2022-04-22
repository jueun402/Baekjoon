# 문제 : https://www.acmicpc.net/problem/11052
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-11052-%EC%B9%B4%EB%93%9C-%EA%B5%AC%EB%A7%A4%ED%95%98%EA%B8%B0

n = int(input()) # 카드의 개수 
p = list(map(int, input().split())) # p 

dp = [0 for _ in range(n+1)]
p = [0]+p

dp[1] = p[1]

for i in range(2,n+1):
    dp[i] = p[i]
    for j in range(1,i):
        dp[i] = max(dp[i], p[j] + dp[i-j])

print(dp[n])

