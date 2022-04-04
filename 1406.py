# 커서를 직관적으로 옮기려는 생각 

import sys

ary = input()
n = int(input())
cursor = len(ary)

for _ in range(n):
    comm = sys.stdin.readline().split()

    if comm[0] == 'L':
        if not cursor:
            cursor -=1

    if comm[0] == 'D':
        if cursor < len(ary):
            cursor +=1
            
    if comm[0] == 'B':
        if not cursor:
            ary.remove(cursor-1) 
    if comm[0] == 'P':
        ary.insert(cursor,comm[1])


# 스택 사용 문제 풀이 

import sys

stack1 = list(input())
stack2 = []
n = int(input())

for _ in range(n):
    comm = sys.stdin.readline().split()

    if comm[0] == 'P':
        stack1.append(comm[1])
    
    if comm[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())

    if comm[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())

    if comm[0] == 'B':
        if stack1:
            stack1.pop()

print("".join(stack1+stack2[::-1]))

