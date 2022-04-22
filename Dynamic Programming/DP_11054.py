# https://www.acmicpc.net/problem/11054
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-11054-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B0%94%EC%9D%B4%ED%86%A0%EB%8B%89-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4#%EC%BD%94%EB%93%9C

n = int(input())
A = list(map(int,input().split())) 
# 감소하는 수열을 증가하는 수열과 한번에 찾기 위해 수열을 뒤집음 
reverseA = A[::-1] 

inc_dp = [1]*n # 증가 dp
dec_dp = [1]*n # 감소 dp

for i in range(n):
    for j in range(i):
        # 증가 수열 
        if A[i] > A[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j]+1)
        
        # 감소 수열 
        if reverseA[i] > reverseA[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j]+1)


# 증가하는 수열 , 감소하는 수열 최대값 찾기 
result = []
for i in range(n):
    result.append(dec_dp[n-i-1] + inc_dp[i]-1)

print(max(result))


# dp = [1]*n

# for i in range(n-1, 0,-1):
#     for j in range(i,n):
#         if A[i] > A[j]:
#             dp[i] = max(dp[i],dp[j]+1)