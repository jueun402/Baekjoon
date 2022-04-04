N = int(input())

arr = []
for i in range(N):
    age, name = list(input().split())
    arr.append((int(age),name))

arr.sort(key = lambda x : x[0])

for i in range(N):
    print(arr[i][0],arr[i][1])