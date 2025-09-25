nombre=input("¿Cual es tu nombre?\n")
edad=int(input("¿Cuantos años tienes? \n"))
altura=float(input("¿Cuanto mides?\n"))
peso=float(input("¿Cuanto pesas?"))

def saludar(nombre):
    return f"Hola {nombre}"

def imc(peso,altura):
    return peso/(altura* altura)


print(saludar(nombre))

print(imc(peso,altura))