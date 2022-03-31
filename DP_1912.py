# https://www.acmicpc.net/problem/1912 
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-1912-%EC%97%B0%EC%86%8D%ED%95%A9

n = int(input())
seq = list(map(int,input().split()))

dp = [0]*n

dp[0] = seq[0]

for i in range(1, n):
    dp[i] = max(seq[i], dp[i-1]+seq[i])

print(max(dp))
