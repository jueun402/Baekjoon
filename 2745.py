# 문제 : https://www.acmicpc.net/problem/2745
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80-2745-%EC%A7%84%EB%B2%95-%EB%B3%80%ED%99%98

N, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
result = 0

for i,n in enumerate(N):
    # print(i,n, end=" ")
    result += (int(b)**i)*(ary.index(n))
    # print(result)

print(result)
