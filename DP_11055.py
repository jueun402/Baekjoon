# https://www.acmicpc.net/problem/11055
n = int(input())
A = list(map(int,input().split()))

dp = A.copy()

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],A[i]+dp[j])

print(max(dp))