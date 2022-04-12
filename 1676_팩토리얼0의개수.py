# 팩토리얼 0의 개수

# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.

# 예제 입력 1 
# 10
# 예제 출력 1 
# 2
# 예제 입력 2 
# 3
# 예제 출력 2 
# 0
#--------------------------풀이 --------------------------------#

def factorial(n):
    return n*factorial(n-1) if n>1 else 1

n = int(input())
result = factorial(n)

cnt = 0
for i in str(result)[::-1]:
    if i =='0' : cnt +=1
    else: break
print(cnt)