espectadores = [(100,"si"), (100,"no"), (10,"no"), (20,"si"), (30,"no")]

entrada = 5000
entradaConDesc = 3500
funciones = 0
funcionesConDescuento = 0
espectadoresConDescuento = 0

i = 0
totalRecaudacion = 0
while i < len(espectadores):
    cantEspectadores, descuento = espectadores[i]
    print(cantEspectadores, descuento)
    if descuento == "si":
        recaudacion = cantEspectadores * entradaConDesc
        espectadoresConDescuento += 1
        funcionesConDescuento += 1
    else:
        recaudacion = cantEspectadores * entrada
    totalRecaudacion += recaudacion
    funciones += 1
    
    i += 1 

porcentajeFuncionesConDescuento = funcionesConDescuento / funciones 
print("total recaudacion: ", totalRecaudacion)
print("funciones: ", funciones, ", funciones con descuento: ", funcionesConDescuento)
print("porcentajeFuncionesConDescuento: ", porcentajeFuncionesConDescuento)
