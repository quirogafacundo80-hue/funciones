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