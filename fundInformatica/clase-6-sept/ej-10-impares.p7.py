ingresado = 17


n = 1
suma = n
print(n, end=", ")

n += 2
while n<=ingresado:
    print(n, end=", ")
    suma += n
    n += 2

print("suma: ", suma)
