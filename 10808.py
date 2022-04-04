ary = str(input())
result = [0]*(ord('z')-ord('a')+1)

for i in ary:
    result[ord(i)-97] +=1 

print(" ".join(str(i) for i in result))
