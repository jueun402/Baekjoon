# https://www.acmicpc.net/problem/11727
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-11727-2n-%ED%83%80%EC%9D%BC%EB%A7%81-2

n = int(input())
dp = [0, 1, 3] 
for i in range(3, n+1): 
    dp.append((dp[i-1] + dp[i-2]*2)%10007) 

print(dp[n])