ary = input()
result = [-1]*(ord('z')-ord('a')+1)

for i in ary:
    result[ord(i)-ord('a')] = ary.find(i)

print(" ".join(str(i) for i in result))