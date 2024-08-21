p = input("Ingrese el número de personas: ")

edad = int(input("Ingrese la edad de las personas : "))
suma_edades = edad
cantidad_personas = 1

for _ in range(1, p):
    edad = int(input("Ingrese la siguiente edad: "))
    suma_edades += edad
    cantidad_personas += 1
