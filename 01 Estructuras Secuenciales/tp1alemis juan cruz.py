# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla 
# un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, 
# el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input ("Ingrese su nombre: ")
print(f"Hola, {nombre}! ")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados.
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, 
# el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input ("Ingrese su nombre:")
apellido = input ("Ingrese su apeliido:")
edad = input ("ingrese su edad:")
lugar_de_residencia = input("ingrese su lugar de residencia:")
print(f"Soy {nombre}{apellido}, tengo {edad} años y vivo en {lugar_de_residencia}. ")

# 4) Crear un programa que pida al usuario el radio de un círculo e 
# imprima por pantalla su área y su perímetro.

radio = float(input(f"ingrese el radio de un círculo")) 
area = 3.1416 * radio ** 2 
perimetro = 2 * 3.1416 * radio 
print(f"El área de un círculo es: {area}  ") 
print(f"El perimetro del círculo es: {perimetro} ")

# 5) Crear un programa que pida al usuario una cantidad de segundos e 
# imprima por pantalla a cuántas horas equivale.
 
segundos = int(input(f"Ingrese segundos:"))
horas = segundos / 3600
print(f"Equivale a {horas} horas.")

#6) Crear un programa que pida al usuario un número e imprima 
#por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un número"))
print(f"{numero} * 0 = ", numero * 0)
print(f"{numero} * 1 = ", numero * 1)
print(f"{numero} * 2 = ", numero * 2)
print(f"{numero} * 4 = ", numero * 4)
print(f"{numero} * 5 = ", numero * 5)
print(f"{numero} * 6 = ", numero * 6)
print(f"{numero} * 7 = ", numero * 7)
print(f"{numero} * 8 = ", numero * 8)
print(f"{numero} * 9 = ", numero * 9)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla 
#el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_1 = int(input("Ingrese un primer número: "))
numero_2 =int(input("Ingrese un segundo número: "))
print(f"{numero_1}+{numero_2} = {numero_1 + numero_2}")
print(f"{numero_1}/{numero_2} = {numero_1 / numero_2}")
print(f"{numero_1}*{numero_2} = {numero_1 * numero_2}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
#Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

altura = float(input("Ingrese su altura"))
peso = float(input("Ingrese su peso")) 
imc = peso / altura ** 2
print(f"Tu IMC es:{imc}")

# 9) Crear un programa que pida al usuario una temperatura 
# en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =95.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temperatura_c = float(input("Ingresa la temperatura en Celsius: "))
temperatura_f = 9/5 * temperatura_c + 32
print("La temperatura en fahrenheit es:", temperatura_f)

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio 
#de dichos números.

numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el segundo número: "))
numero_3 = int(input("Ingresa el tercer número: "))

promedio = (numero_1 + numero_2 + numero_3) / 3
print(f"El promedio de los números {numero_1}, {numero_2} y {numero_3} es: {promedio}")



