import sys


while True:

    inline = sys.stdin.readline().rstrip('\n')

    if not inline:
        break

    result = [0]*4
    for i in inline:
        # 소문자 
        if i.islower():
            result[0] +=1
        # 대문자
        elif i.isupper():
            result[1] +=1
        # 숫자 
        elif i.isdigit():
            result[2] +=1
        # 공백
        elif i.isspace():
            result[3] +=1

    print(" ".join(str(i) for i in result))