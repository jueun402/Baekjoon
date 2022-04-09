
# 문제 : https://www.acmicpc.net/problem/11005
# 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80-10989-%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3
n,b = map(int,input().split())
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result=""

while True:

    if n==0:
        break
    
    result+=str(ary[n%b])
    n=n//b

print(result[::-1])
