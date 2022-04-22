import sys

N = int(input())

myDict = {}

for _ in range(N):
    num = int(input())

    if num not in myDict.keys():
        myDict[num] =1
    else:
        myDict[num] +=1

sDict = sorted(myDict.items(), key = lambda x : (-x[1], x[0]))

print(sDict[0][0])
