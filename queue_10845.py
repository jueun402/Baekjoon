import sys

n = int(sys.stdin.readline().rstrip())

queue = []
for _ in range(n):
    ary = sys.stdin.readline()

    if "push" in ary:        
        queue.append(int(ary.split()[1]))

    if 'pop' in ary:       
        if queue:
            print(queue.pop(0))
        else:
            print('-1')

    if 'size' in ary: 
        print(len(queue))       

    if 'empty' in ary:        
        if queue:
            print('0')
        else:
            print('1')

    if 'front' in ary:
        if queue:    
            print(queue[0])    
        else:
            print('-1')
    
    if 'back' in ary: 
        if queue:
            print(queue[-1])
        else:
            print('-1')
