
# 문제 : https://www.acmicpc.net/problem/9095
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-9095-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0
t = int(input())
dp = [0,1,2,4]

for i in range(4,11):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in range(t):
    n = int(input())
    print(dp[n])