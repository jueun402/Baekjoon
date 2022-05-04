
from collections import defaultdict

def solution(id_list, report, k):
    key =  list(map(lambda x : x.split()[0], report)) # 신고자
    value = list(map(lambda x : x.split()[1], report))  # 신고당한 유저 

    repo_dict = defaultdict(list) # 신고 report 
    stop_user = defaultdict(list) # 정지 유저 

    for i,v in zip(key,value):
        # 이미 동일한 유저를 신고했다면 continue 
        if v in repo_dict[i]:
            continue     
        
        repo_dict[i].append(v)
        stop_user[v].append(i)

    result = {}.fromkeys(id_list,0)

    # stop user를 지목한 user의 길이를 구하자         
    for usr in list(stop_user.items()):
        if len(usr[1])>=k:
            for i in usr[1]:
                result[i] +=1        

    return list(result.values())