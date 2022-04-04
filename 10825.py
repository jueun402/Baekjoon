N = int(input())

arr = []
for _ in range(N):
    name, kor, eng, math = list(input().split())
    arr.append((str(name),int(kor),int(eng),int(math)))

arr.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(arr[i][0])