import sys
from itertools import combinations

def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

t = int(input())

for _ in range(t):
    ary = list(map(int,sys.stdin.readline().split()))

    comb = list(combinations(ary[1:],2))

    result = 0  
    for i in comb:
        result += gcd(i[0],i[1])

    print(result)
    
    