with open('./class6/test.ini','rt',encoding='utf-8') as F:
    for line in F:
        if line=='[languages]':
            continue
        else:
            print(line)
