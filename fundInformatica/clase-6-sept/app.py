n = -1234567
n = abs(n)

digitos = 1
while n//10>0:
    digitos += 1
    n = n//10

print(digitos)