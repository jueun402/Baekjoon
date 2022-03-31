# https://www.acmicpc.net/problem/11053
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-11053-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4

n = int(input())

A = list(map(int, input().split()))

dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j]+1)
  
print(max(dp))
