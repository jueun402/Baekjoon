ary = input()

stack = []
result = 0

for i in range(len(ary)):

    if ary[i] == '(':
        stack.append(ary[i])
    
    elif ary[i]==')':
        stack.pop(-1)

        # ))가 나왔을 때 
        if ary[i-1] == ')':
            result +=1
        else:
            result +=len(stack)

print(result)