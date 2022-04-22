inline = input()


result = ""

for w in inline:
    # 대문자
    if w.isupper():
        # 13을 더했을 때 값이 Z보다 크다면 
        if ord(w)+13 > ord('Z') :
            result += chr((ord(w)+13)%ord('Z') + (ord('A')-1))
        else:
            result +=chr(ord(w)+13)

    # 소문자 
    elif w.islower():
        # 13을 더했을 때 값이 z보다 크다면 
        if ord(w)+13 > ord('z'):
            result +=chr((ord(w)+13)%ord('z') + (ord('a')-1))

        else:
            result +=chr(ord(w)+13)

    else:
        result += w

print(result)