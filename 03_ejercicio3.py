def presentar_persona(nombre="Nacho",age="None",*aficiones):

    return f"Hola {nombre},tienes {age} años y tus aficiones son: {aficiones}"


print(presentar_persona("Ana",25,"Futbol","Programar","Hockey"))