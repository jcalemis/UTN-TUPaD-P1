#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):  # El rango empieza en 0 y termina en 100
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

numero = int(input("Ingresa un número entero: "))  # Solicita al usuario un número
cantidad_digitos = len(str(abs(numero)))  # Convierte el número a cadena y cuenta los caracteres
print(f"El número tiene {cantidad_digitos} dígitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

# Solicitar los valores al usuario
inicio = int(input("Ingresa el primer número: "))
fin = int(input("Ingresa el segundo número: "))

# Asegurar que inicio sea menor que fin
if inicio > fin:
    inicio, fin = fin, inicio  # Intercambia valores si están en orden inverso

# Calcular la suma de los números en el rango excluyendo los extremos
suma = sum(range(inicio + 1, fin))

print(f"La suma de los números entre {inicio} y {fin}, excluyendo los extremos, es: {suma}")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

# Inicializar la suma acumulada
suma_total = 0

# Bucle infinito para recibir números
while True:
    numero = int(input("Ingresa un número entero (0 para finalizar): "))
    
    if numero == 0:  # Condición de salida
        break
    
    suma_total += numero  # Acumular la suma

# Mostrar el resultado final
print(f"La suma total de los números ingresados es: {suma_total}")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

# Generar un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0

print("¡Bienvenido al juego de adivinanza!")
print("Debes adivinar un número entre 0 y 9.")

while True:
    intento = int(input("Ingresa tu número: "))  # Solicitar un número al usuario
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Intenta de nuevo.")

