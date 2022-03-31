
n = int(input())

# 최솟값을 찾아야하기 때문에 0으로 초기화 불가! 
dp = [i for i in range(n+1)] 

for i in range(4, n+1):
    for j in range(1,i):
        
        if j*j > i:
            break

        if dp[i] > dp[i-(j*j)] +1:
            dp[i] = dp[i-(j*j)] +1

print(dp[n])
