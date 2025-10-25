def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero_tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)