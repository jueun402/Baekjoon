ary = input()

result = []
for i in range(len(ary)):
    result.append(ary[i:])

result.sort()

for i in result:
    print(i)