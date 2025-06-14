#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1) 


num = int(input("Ingrese un numero entero: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} es {factorial(i)}")


#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.


def serie_fibo(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return serie_fibo(x-1) + serie_fibo(x-2)


pos = int(input("Ingrese una posicion: "))

for i in range(pos + 1):
    print(f"Posición {i}: {serie_fibo(i)}")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛
#𝑚 = 𝑛 ∗ 𝑛
#(𝑚−1)
#. Prueba esta función en un
#algoritmo general.


def potencia(base, exponente):
    if (base == 0) and (exponente == 0):
        return "Error: 0^0 no está definido"
    elif base == 0:
        return 0
    elif exponente == 0:
        return 1
    elif exponente < 0:
        return "Error: exponente negativo"
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
    
print(f"La potencia de {base} elevado a {exponente} es: {potencia(base,exponente)}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.


def conversion(num):
    if num == 0:
        return "0"
    else:
        cociente = num // 2     
        resto = str(num % 2)    
        return conversion(cociente) + resto     

num = int(input("Ingrese un numero entero: "))

print(f"El numero {num} en binario es: {conversion(num)}")


