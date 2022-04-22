import sys

def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

T = int(input())

for _ in range(T):
    a,b = sys.stdin.readline().split()
    print(lcm(int(a),int(b)))