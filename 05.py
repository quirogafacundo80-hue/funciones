def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f} horas")