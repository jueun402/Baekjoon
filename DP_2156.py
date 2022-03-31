# https://www.acmicpc.net/problem/2156
#  풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-2156-%ED%8F%AC%EB%8F%84%EC%A3%BC-%EC%8B%9C%EC%8B%9D

# n 입력 
n = int(input())

# 포도주 양 입력 
wine = [0]
for _ in range(n):
    wine.append(int(input()))

dp=[0]*(n+1)
dp[1] = wine[1]

if n >=2:
    dp[2] = wine[1]+wine[2]
if n >=3:
    dp[3] = max(dp[2], wine[1]+wine[3], wine[2]+wine[3])

for i in range(4,n+1):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i]+wine[i-1])
    
print(dp[n])

