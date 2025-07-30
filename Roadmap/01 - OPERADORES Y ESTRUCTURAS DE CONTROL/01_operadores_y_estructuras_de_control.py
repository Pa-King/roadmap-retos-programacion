### operadores y estructuras de control ###

# Operadores aritméticos

print(f"suma = 5 + 3 = {5 + 3}") # Operador de suma, imprime cadena de texto y resultado
sum = 10 + 3 # Asignación de la suma a una variable
print(sum) # Imprime solo el valor (resultado) de la variable sum

print(f"resta = 10 - 4 = {10 - 4}")
resta = 10 - 4
print(resta)

print(f"multiplicacion = 2 * 6 = {2 * 6}")
multiplicacion = 2 * 6
print(multiplicacion)

print(f"division = 8 / 2 = {8 / 2}")
division = 8 / 2
print(division)

print(f"division entera = 8 // 3 = {8 // 3}")
division_entera = 8 // 3
print(division_entera)

print(f"modulo = 10 % 3 = {10 % 3}")
modulo = 10 % 3
print(modulo)

print(f"potencia = 2 ** 3 = {2 ** 3}") # Operador de potencia
potencia = 2 ** 3
print(potencia)

# Operadores de comparación

print(f"igualdad = 5 == 5 = {5 == 5}")
igualdad = 5 == 5
print(igualdad) #igual que los operadores aritméticos, pueden utilizarse de igual forma

print(f"desigualdad = 5 != 5 = {5 != 5}")
print(f"mayor que = 5 > 3 = {5 > 3}")
print(f"menor que = 5 < 3 = {5 < 3}")
print(f"mayor o igual que = 5 >= 5 = {5 >= 5}")
print(f"menor o igual que = 5 <= 5 = {5 <= 5}")

# Operadores lógicos

print(f"and = True and False = {True and False}") # Operador lógico AND
print(f"ANF && = 10 + 3 == 13 && 5 > 3 = {10 + 3 == 13 and 5 > 3}") # AND con expresiones
print(f"or = True or False = {True or False}") # Operador lógico OR
print(f"OR || = 10 + 3 == 13 || 5 < 3 = {10 + 3 == 13 or 5 < 3}") # OR para dar TRUE solo pide que una de las condiciones sea TRUE
print(f"not = not True = {not True}") # Operador lógico NOT, invierte el valor booleano
print(f"NOT ! = not (10 + 3 == 13) = {not (10 + 3 == 13)}") # NOT con expresión, invierte el resultado de la expresión

# operadores de asignación

my_number = 10 # Asignación simple
print(f"my_number = {my_number}")
my_number += 5 # Asignación con suma, equivale a my_number = my_number + 5
print(f"my_number += 5 = {my_number}")
my_number -= 3 # Asignación con resta, equivale a my_number = my_number - 3
print(f"my_number -= 3 = {my_number}")
my_number *= 2 # Asignación con multiplicación, equivale a my_number = my_number * 2
print(f"my_number *= 2 = {my_number}")
my_number /= 4 # Asignación con división, equivale a my_number = my_number / 4
print(f"my_number /= 4 = {my_number}")
my_number //= 2 # Asignación con división entera, equivale a my_number = my_number // 2
print(f"my_number //= 2 = {my_number}")
my_number %= 2 # Asignación con módulo, equivale a my_number = my_number % 3
print(f"my_number %= 3 = {my_number}")
my_number **= 2 # Asignación con potencia, equivale a my_number = my_number ** 2
print(f"my_number **= 2 = {my_number}")

# operadores de identidad

my_new_number = 1.0 # Asignación de un nuevo número
print(f"my_new_number is my_number es {my_new_number is my_number}") # Operador de identidad IS, verifica si dos variables apuntan al mismo objeto
my_new_number = my_number # Asignación de la misma referencia
print(f"my_new_number is my_number es {my_new_number is my_number}") # Ahora ambas variables apuntan al mismo objeto

# operadores de pertenencia

my_list = [1, 2, 3, 4, 5] # Definición de una lista
print(f"1 in my_list es {1 in my_list}") # Operador IN, verifica si un elemento está en una colección
print(f"6 not in my_list es {6 not in my_list}") # Operador NOT IN, verifica si un elemento no está en una colección    
print(f"my_list[0] = {my_list[0]}") # Imprime el primer elemento de la lista

# operadores de bits

print(f"5 & 3 = {5 & 3}") # Operador AND bit a bit
a = 5 # Asignación de un valor a a
b = 3 # Asignación de un valor a b
print(f"a & b = {a & b}") # Imprime el resultado de a AND b
print(f"5 | 3 = {5 | 3}") # Operador OR bit a bit
print(f"a | b = {a | b}") # Imprime el resultado de a OR b
print(f"5 ^ 3 = {5 ^ 3}") # Operador XOR bit a bit
print(f"a ^ b = {a ^ b}") # Imprime el resultado de a XOR b
print(f"5 << 1 = {5 << 1}") # Operador de desplazamiento a la izquierda
print(f"a << 1 = {a << 1}") # Imprime el resultado de a desplazado a la izquierda
print(f"5 >> 1 = {5 >> 1}") # Operador de desplazamiento a la derecha
print(f"a >> 1 = {a >> 1}") # Imprime el resultado de a desplazado a la derecha
print(f"~5 = {~5}") # Operador NOT bit a bit

# operadores de prioridad

print(f"5 + 3 * 2 = {5 + 3 * 2}") # Multiplicación tiene mayor prioridad que suma
print(f"(5 + 3) * 2 = {(5 + 3) * 2}") # Paréntesis cambian el orden de evaluación
print(f"5 + 3 > 2 * 4 = {5 + 3 > 2 * 4}") # Comparación con operadores de prioridad
print(f"5 + 3 > 2 * 4 and 10 < 20 = {5 + 3 > 2 * 4 and 10 < 20}") # AND con operadores de prioridad
print(f"not (5 + 3 > 2 * 4) = {not (5 + 3 > 2 * 4)}") # NOT con operadores de prioridad

### Estructuras de control ###

# Condicionales

my_string = "Francisco" # Asignación de una cadena de texto
if my_string == "Francisco": # Condición para verificar si my_string es igual a "Francisco"
    print("my_string es igual a Francisco") # Imprime si la condición es verdadera
elif my_string == "Panchito": # Condición alternativa si la primera no se cumple
    print("my_string es igual a Panchito")
else: # Condición alternativa si ninguna de las anteriores se cumple
    print("my_string no es igual a Francisco ni a Panchito")

my_string = "Panchito" # Cambio de valor de my_string
if my_string == "Francisco": # Verifica nuevamente la condición
    print("my_string es igual a Francisco") # Imprime si la condición es verdadera
elif my_string == "Panchito": # Verifica la segunda condición
    print("my_string es igual a Panchito") # Imprime si la segunda condición es verdadera
else: # Si ninguna de las condiciones anteriores se cumple
    print("my_string no es igual a Francisco ni a Panchito") # Imprime si ninguna condición es verdadera

# Iterativas

for i in range(11): # Bucle for que itera desde 0 hasta 10
    print(f"i = {i}") # Imprime el valor de i en cada iteración

i = 0 # Inicialización de la variable i

while i < 11: # Bucle while que se ejecuta mientras i sea menor que 11
    print(f"i = {i}") # Imprime el valor de i en cada iteración
    i += 1 # Incrementa i en 1 en cada iteración

# Manejo de excepciones

try:
    print(10/0) # Intenta dividir 10 entre 0, lo que generará una excepción
except:
    print("Error: No se puede dividir por cero")
finally:
    print("el proceso a finalizado") # Este bloque se ejecuta siempre, independientemente de si hubo una excepción o no

### Extra ###

for i in range(10, 56): # Bucle for que itera desde 10 hasta 55
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(f"i = {i}") # Imprime i si es par, no es 16 y no es múltiplo de 3
        