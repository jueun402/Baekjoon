n, k = map(int,(input().split()))

ary = list(range(1,n+1))
result = [] # 제거된 사람들 list 
index = 0 # 순서 index

while True:

    index += k-1 # 배열이 1부터 시작하기때문에 index값은 k-1 

    # ary가 빌 때 까지 while문 순회 
    try:
        if index >= len(ary):
            index = index%len(ary)

        # print("index : " ,index)
        # print(ary.pop(index))
        result.append(str(ary.pop(index)))

    except:
        break

print("<"+", ".join(i for i in result)+">")