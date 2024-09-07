d = 6
m = 9
anio = 2024
print(d,m,anio)

n = 135

i = 0
while i < n:
    d += 1
    if m==2 and d==29:
        m += 3
        d = 1
    elif d==31 and (m==4 or m==6 or m==9 or m==11):
        d=1
        m += 1
    elif d==32 and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        d = 1
        if m==12:
            m = 1
            anio += 1
        else:
            m += 1
        
    i += 1

print(d,m,anio)
