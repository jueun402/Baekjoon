import sys
from collections import deque

n = int(input())
dq = deque([])

for _ in range(n):
    ary =sys.stdin.readline().split()

    if ary[0] == 'push_front':
        dq.appendleft(ary[1])

    if ary[0] == 'push_back':
        dq.append(ary[1])

    if ary[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print('-1')

    if ary[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print('-1')

    if ary[0] == 'size':
        print(len(dq))

    if ary[0] == 'empty':
        if dq:
            print('0')
        else:
            print('1')

    if ary[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print('-1')

    if ary[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print('-1')
