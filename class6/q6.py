sysdirt={}
with open('./class6/test.ini','rt',encoding='utf-8') as F:
    next(F)
    for line in F:
        a=line.strip().split('=')
        print(a)
        sysdirt[a[0]]=a[1]
print(sysdirt)
