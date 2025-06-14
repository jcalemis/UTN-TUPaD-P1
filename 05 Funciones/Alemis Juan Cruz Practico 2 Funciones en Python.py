#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

# Definición de la función
def imprimir_hola_mundo():
  print("Hola Mundo!")

# Programa principal
if __name__ == "__main__":
   imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.


# Definición de la función
def saludar_usuario(nombre):
 return f"Hola {nombre}!"

# Programa principal
if __name__ == "__main__":
 nombre_usuario = input("Por favor, ingresa tu nombre: ")
 saludo = saludar_usuario(nombre_usuario)
 
print(saludo)

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.


# Definición de la función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("¿Dónde vives?: ")

    informacion_personal(nombre, apellido, edad, residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del
#círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.


import math

# Función para calcular el área del círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Función para calcular el perímetro del círculo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
if __name__ == "__main__":
    radio = float(input("Ingresa el radio del círculo: "))

    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.


# Función para convertir segundos a horas
def segundos_a_horas(segundos):
     return segundos / 3600

# Programa principal
if __name__ == "__main__":
     segundos = int(input("Ingresa la cantidad de segundos: "))
     horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")


#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.


# Función para imprimir la tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
     resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Programa principal
if __name__ == "__main__":
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)


#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
#restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.


# Función que realiza operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

# Programa principal
if __name__ == "__main__":
    try:
         a = float(input("Ingresa el primer número: "))
         b = float(input("Ingresa el segundo número: "))

         resultados = operaciones_basicas(a, b)

         print(f"Suma: {resultados[0]}")
         print(f"Resta: {resultados[1]}")
         print(f"Multiplicación: {resultados[2]}")
         print(f"División: {resultados[3]}")

    except ValueError:
       print("Por favor, ingresa valores numéricos válidos.")


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


# Función para calcular el IMC
def calcular_imc(peso, altura):
  return peso / (altura ** 2)

# Programa principal
if __name__ == "__main__":
    try:
          peso = float(input("Ingresa tu peso en kilogramos: "))
          altura = float(input("Ingresa tu altura en metros: "))
 
          imc = calcular_imc(peso, altura)
          print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
 
    except ValueError:
         print("Por favor, ingresa valores numéricos válidos.")
    except ZeroDivisionError:
          print("La altura no puede ser cero.")


#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.


# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
if __name__ == "__main__":
     try:
         celsius = float(input("Ingresa la temperatura en grados Celsius: "))
         fahrenheit = celsius_a_fahrenheit(celsius)
         print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
     except ValueError:
       print("Por favor, ingresa un valor numérico válido.")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.


# Función para calcular el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":
    try:
         a = float(input("Ingresa el primer número: "))
         b = float(input("Ingresa el segundo número: "))
         c = float(input("Ingresa el tercer número: "))
  
         promedio = calcular_promedio(a, b, c)
         print(f"El promedio de los tres números es: {promedio:.2f}")
 
    except ValueError:
          print("Por favor, ingresa valores numéricos válidos.")


