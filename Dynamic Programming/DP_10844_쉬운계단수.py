
# https://www.acmicpc.net/problem/10844
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-10844-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98

n = int(input())

# 2차원 배열로 생성 
# dp[N][끝자리 숫자] = 개수
dp = [[0]*10 for _ in range(n+1)] 
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2,n+1):
    # 끝자리 0인 경우 
    dp[i][0] = dp[i-1][1]

    # 끝자리 9인 경우 
    dp[i][9] = dp[i-1][8]

    for j in range(1,9):
        dp[i][j] =dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)
