def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()



def saludar_usuario(nombre):
    return f"Hola {nombre}!"


nombre_usuario = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_usuario))


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su ciudad de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}")


def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f} horas")



def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero_tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)



def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por 0"
    return suma, resta, multiplicacion, division

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


def calcular_imc(peso, altura):
    if altura <= 0:
        return "Altura no puede ser 0 o negativa"
    imc = peso / (altura ** 2)
    return round(imc, 2)

try:
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    resultado = calcular_imc(peso, altura)
    print(f"Su IMC es: {resultado}")
except ValueError:
    print("Debe ingresar números válidos para peso y altura.")

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))
print(f"Equivalente en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}°F")



def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
print(f"El promedio es: {calcular_promedio(num1, num2, num3):.2f}")
