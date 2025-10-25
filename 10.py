def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
print(f"El promedio es: {calcular_promedio(num1, num2, num3):.2f}")