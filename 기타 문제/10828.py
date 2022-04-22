
import sys

n = int(input())

stack = []

for _ in range(n):
    comm = sys.stdin.readline()

    if 'push' in comm :
        stack.append(int(comm.split()[1]))

    if 'pop' in comm:
        try:
            print(stack.pop())
        except:
            print('-1')

    if 'size' in comm:
        print(len(stack))

    if 'top' in comm:
        try:
            print(stack[-1])
        except:
            print('-1')

    if 'empty' in comm:
        if len(stack) ==0:
            print('1')
        else:
            print('0')