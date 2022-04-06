
n,b = map(int,input().split())
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result=""

while True:

    if n==0:
        break
    
    result+=str(ary[n%b])
    n=n//b

print(result[::-1])

