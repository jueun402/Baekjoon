# https://www.acmicpc.net/problem/9461
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-9261-%ED%8C%8C%EB%8F%84%EB%B0%98-%EC%88%98%EC%97%B4


T = int(input())

dp = [1]*101

for i in range(4,101):
    dp[i] = dp[i-2]+dp[i-3]

for i in range(T):
    n = int(input())
    print(dp[n])
    