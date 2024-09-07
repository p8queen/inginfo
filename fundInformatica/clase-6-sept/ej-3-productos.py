unidades = 230
auxUnidades = unidades
base = 100

total = 0
i = 1
while unidades > 0 and i < 13:
    total += base
    unidades -= 1
    i += 1

while unidades > 0 and i < 101:
    total += base*.9
    unidades -= 1
    i += 1

while unidades > 0 :
    total += base*.75
    unidades -= 1
    i += 1

promedio = total/auxUnidades
print("total: ", total)
print("promedio: ", promedio)

