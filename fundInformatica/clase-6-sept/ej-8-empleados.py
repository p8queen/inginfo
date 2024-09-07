''' · Importe total de salarios pagados por la empresa.
· Cantidad de empleados que ganan más de $200000.
· Cantidad de empleados que ganan menos de $50000, cuya categoría sea
3.
· Legajo del empleado que más gana.
· Sueldo más bajo.
· Importe total de sueldos por cada categoría.
· Salario promedio
'''

empleados = [(11,1,300000),(12,2,80000),(13,3,45000),(14,1,400000),(15,2,450000),(16,2,30000),(17,3,120000)]

# Importe total de salarios pagados por la empresa.
totalSalarios = 0

# Cantidad de empleados que ganan más de $200000.
# Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3
cantEmpleadosMas200 = 0
cantEmpleadosMenos50Cat3 = 0

# Legajo del empleado que más gana.
maxSalario = 0
legajoEmpleadoMasGana = 0

sueldoMasBajo = 0

# · Importe total de sueldos por cada categoría.
totalCategoria1 = 0
totalCategoria2 = 0
totalCategoria3 = 0

i=0
while i<len(empleados):
    legajo, categoria, salario = empleados[i]
    totalSalarios += salario
    if categoria == 1:
        totalCategoria1 += salario
    elif categoria == 2:
        totalCategoria2 += salario
    else:
        totalCategoria3 += salario
    
    if salario > 200000:
        cantEmpleadosMas200 += 1
    elif salario < 50000 and categoria == 3:
        cantEmpleadosMenos50Cat3 += 1
    
    if salario > maxSalario:
        legajoEmpleadoMasGana = legajo
    
    if sueldoMasBajo == 0:
        sueldoMasBajo = salario
    elif salario < sueldoMasBajo:
        sueldoMasBajo = salario
        
    i += 1

promedioSalarios = totalSalarios / i
print("totalSalarios: ", totalSalarios)
print("promedioSalarios: ", promedioSalarios)
print("cantEmpleadosMas200: ", cantEmpleadosMas200)
print("cantEmpleadosMenos50Cat3: ", cantEmpleadosMenos50Cat3)
print("legajoEmpleadoMasGana: ", legajoEmpleadoMasGana)
print("sueldoMasBajo: ", sueldoMasBajo)
print("total x categorias: ", totalCategoria1, totalCategoria2, totalCategoria3)


