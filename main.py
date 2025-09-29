import sys

def main():
    # sys.argv es una lista con los argumentos de la línea de comandos
    # El primer elemento (posición 0) es siempre el nombre del archivo
    print("Argumentos recibidos:", sys.argv)

    # Si hay argumentos adicionales, los mostramos
    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        ciudad=sys.argv[2]
        edad=sys.argv[3]
        print(f"Hola, {nombre} 👋")
        print(f"Vives en {ciudad} ")
        print(f"Tienes {edad} años ")
    else:
        print("No se proporcionó ningún argumento")

if __name__ == "__main__":
    main()