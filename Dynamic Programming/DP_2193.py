# 2193번 (이친수) -> dp

'''
0과 1로만 이루어진 수 = 이진수 
이친수 
- 0으로 시작 x 
- 1이 두 번 연속으로 나타나지 않는다. 11을 부분 문자열로 갖지 않는다. 
- N자리 이친수의 개수를 출력

규칙을 따라 이천수를 구해보면 패턴이 반복됨.
    1. N은 N-1의 결과에 + 0을 더한 것과 N-1의 결과에 01을 추가한 것과 동일함  
    2. N의 개수는 N-1의 결과와 N-2의 결과의 합과 동일함 => 피보나치 수열 
    3. 피보나치 개수 구하는 방식으로 N자리 이천수의 개수 출력  
'''
N = int(input()) 
result = [0 for _ in range(N+1)] 

for i in range(1,N+1):
    if i ==1 or i==2:
        result[i]=1
    else:
        result[i] = result[i-1]+result[i-2]
print(result[N])