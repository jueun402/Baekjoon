# https://www.acmicpc.net/problem/1463
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-1463-1%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0

#정수 n 입력받기 
n = int(input())

#DP 테이블 초기화 
dp = [0]*(n+1) 

for i in range(2,n+1):

    # 현재 수에서 1을 빼는 경우
    dp[i] = dp[i-1]+1
    # 현재 수가 3으로 나눠지는 경우 
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1) 
    # 현재 수가 2로 나눠지는 경우 
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] +1)    

print(dp[n])
