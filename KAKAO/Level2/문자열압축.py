def solution(s):
    answer = 10**10
    # 1~ s//2만큼의 간격으로 나눔 
    for i in range(1,len(s)//2+1):
        ans = []	
        before = s[0:i] # 초기값 
        k ,cnt = i, 1 # k = i부터 시작 , cnt = count 
        ans.append(str(cnt)+before)

        for j in range(i+k,len(s)+i,i):

            now = s[k:j] # 현재값
            k = j   # 간격 조절 
            
            # 직전 값과 현재 값이 동일하면 
            if now == before:
                cnt = int(ans[-1][0]) +1 # 직전값의 cnt +1  
                before = now 
                ans[-1] = str(cnt)+before  
                continue
            
            # 직전값과 현재값이 다르면 
            else: 
                cnt = 1 
                before = now
                ans.append(str(cnt)+now)
        print(ans)
        result = 0
        for a in ans:
            if '1' in a:  result += len(a)-1
            else: result += len(a)
                    
        answer = min(result, answer)
    
    return answer

s = "aabbaccc"
solution(s)


'''
압축할 문자열 s가 매개변수로 주어질 때, 
위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 
압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 
하도록 solution 함수를 완성해주세요.

s = "aabbaccc"	=> 2a2ba3c
result = 7

'''
s = "aabbaccc"

ans = []
i, cnt = 0, 1 # 초기 index, cnt값 

for j in range(1,len(s)):
    print(s[j])
    if s[i] == s[j]:
        # print(s[i], s[j])
        cnt +=1
    else:
        # print(str(cnt)+s[i])
        ans.append(str(cnt)+s[i])
        i = j
        cnt = 1
        continue















# 문자열 1개 단위로 잘라 압축 
ans = []
j = 0
for i in range(len(s)):
    i = j
    cnt = 1
    for j in range(i+1,len(s)):

        # 
        if s[i] == s[j]:
            cnt +=1
        else:
            print(str(cnt)+s[i])
            ans.append(str(cnt)+s[i])
            break

j

"abcabcdede"	=> len('2abcded2')
"abcabcabcabcdededededede"	
len("xababcdcdababcdcd"	)

# 1 단위로 나누는 것 
for i in range(1,len(s)):
    print(s[i-1], s[i])
    print(i)
    

#-------------------------------test----------------------------
s = "abcabcabcabcdededededede"	
len(s)//2
s[:2]

# 최소 1개 단위에서 반절 단위로 나눌 수 있음 / len(s)//2
s = "aabbaacc"	

k = 0
# 2의 간격으로 나눔 
for i in range(2,len(s)+1,2):
    print(s[k:i])
    k = i

# 3의 간격으로 나눔 
k = 0
for i in range(3,len(s)+1,3):
    print(s[k:i])
    k = i

# 4의 간격으로 나눔 
k = 0
for i in range(4,len(s)+1,4):
    print(s[k:i])
    k = i

s = "abcabcabcabcdededededede"	

ans =[[] for i in range(0,(len(s)//2)+1)]

# 1~ s//2만큼의 간격으로 나눔 
for i in range(1,len(s)//2+1):
    k = 0
    for j in range(i,len(s)+1,i):
        ans[i].append(s[k:j])
        # print(s[k:j])
        k = j   


ans =[[] for i in range(0,(len(s)//2)+1)]


ans = [[], [[1, 'a'], [1, 'a'], [1, 'b'], [1, 'b'], [1, 'a'], [1, 'c'], [1, 'c'], [1, 'c']], [[1, 'aa'], [1, 'bb'], [1, 'ac'], [1, 'cc']], [[1, 'aab'], [1, 'bac']], [[1, 'aabb'], [1, 'accc']]]  

s ="xababcdcdababcdcd"						
answer = 10**10
# 1~ s//2만큼의 간격으로 나눔 
for i in range(1,len(s)//2+1):
    ans = []	
    before = s[0:i] # 초기값 
    k ,cnt = i, 1 # k = i부터 시작 , cnt = count 
    ans.append(str(cnt)+before)

    for j in range(i+k,len(s)+i+1,i):

        now = s[k:j] # 현재값
        k = j   # 간격 조절 
        
        # 직전 값과 현재 값이 동일하면 
        if now == before:
            cnt = int(ans[-1][0]) +1 # 직전값의 cnt +1  
            before = now 
            ans[-1] = str(cnt)+before  
            # print(ans)
            continue
        
        # 직전값과 현재값이 다르면 
        else: 
            cnt = 1 
            before = now
            ans.append(str(cnt)+now)
    
    print(ans)
    result = 0
    for a in ans:
        if '1' in a:  result += len(a)-1
        else: result += len(a)
                
    answer = min(result, answer)
    
    
    
       
        # 직전에 추가한 값이랑 현재 값이랑 비교 
        try:
            if ans[-1][-1][1] == s[k:j]:
                print(s[k:j])
                cnt +=1            
        except:
            ans[i].append([cnt,s[k:j]])
        # print(s[k:j])
        k = j   



