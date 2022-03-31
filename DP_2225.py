# https://www.acmicpc.net/problem/2225
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-2225-%ED%95%A9%EB%B6%84%ED%95%B4

n, k = map(int, input().split())

dp = [[0]*201 for i in range(201)]

# k = 1, n =1 초기화 
for i in range(201):
    dp[i][1] = i
    dp[1][i] = 1

for i in range(2,201):
    for j in range(2,201):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]

print(dp[k][n]%1000000000)