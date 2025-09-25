import math
entrada=input("Introduce tu operacion:")
operacion=entrada.split(" ")
contador=0
numero1=0
numero2=0
operador=0

try:
    numero1=int(operacion[0])
    numero2=int(operacion[2])
    operador=operacion[1]
except ValueError:
    print("Valor no numerico introducido")
except IndexError:
    print("Numero de valores incorrecto")

resultado=0
match operador:
       case "+":
           resultado=numero1+numero2
       case "-":
           resultado=numero1+numero2
       case "/":
           resultado=numero1/numero2
       case "*":
           resultado=numero1*numero2
       case _:
          print(f"Operador {operador}, utiliza *,+,-,/")

print(resultado)
