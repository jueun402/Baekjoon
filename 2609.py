a,b = list(map(int,input().split()))

# 최대 공약수
def gcd(a,b):
    while b > 0:
        a, b = b, a%b    
    print(a)
    return  a

# 최소 공배수
def lcm(a,b):
    print(a*b//gcd(a,b))

    
lcm(a,b)