num = 1234
print(num)
capicua = 0
factor = 0
while num != 0:
    if factor == 0:
        capicua = num % 10
    else:
        capicua = capicua*10 + (num % 10) 
    num = num//10
    factor += 1
    print(capicua, num)