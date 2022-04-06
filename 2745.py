n, b = input().split()
ary = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0

while n!=0:
    result +=str(ary[n%b])
    n = n//b

for i in ary:
    ary

    n*b