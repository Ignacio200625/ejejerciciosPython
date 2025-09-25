
entrada=input("Introduce una lista de enteros separado por comas:")
numeros=entrada.split(",")
maximo=0
suma=0
minimo=0
promedio=0
contador=0
bandera=False
for i in range(len(numeros)):
    numeros[i]=int(numeros[i])
for i in range(len(numeros)):
    if(not bandera):
        minimo=numeros[i]
        bandera=True
    if(maximo<numeros[i]):
        maximo=numeros[i]
    if(minimo>numeros[i] and bandera):
        minimo=numeros[i]
    suma=suma+numeros[i]
    contador=contador+1

promedio=suma/contador

print(maximo)
print(minimo)
print(promedio)
print(suma)