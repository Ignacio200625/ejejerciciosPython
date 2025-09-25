while True:
    try:
        edad=int(input("¿Cuantos años tienes? \n"))
        altura=float(input("¿Cuanto mides?\n"))
        break
    except ValueError:
        print("Valor incorrecto")
    
