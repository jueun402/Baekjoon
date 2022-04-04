n = int(input())

for _ in range(n):
    ary = list(input())
    stack=[]

    for i in ary:
        if i =='(': # '('가 들어오면 STACK에 넣음 
            stack.append(i)
        elif i == ')': # ')'가 들어오면 STACK POP 
            if stack:
                stack.pop()
            else:       # ')'가 들어왔는데 STACK에 '('이 없으면 NO
                print("NO")
                break
    else:
        if stack: # 문자열 검사를 다 했는데, 스택에 '(', ')'가 남아있다면 
           print("NO") 
        else:
            print("YES")