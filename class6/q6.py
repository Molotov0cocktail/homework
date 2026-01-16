with open('./class6/test.ini','rt',encoding='utf-8') as F:
    next(F)
    for line in F:
        print(line)
