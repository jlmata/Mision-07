#Autor: Jose Luis Mata Lomelí
#Matricula: A01377205

#Menu con las opciones de dividir mediante restas multiples y
# encontrar el numero mayor de n numeros dados por el usuario

#Menu de opciones
def leerMenu():
    print(" ")
    print("Mision 7: Ciclos while")
    print("Autor: Jose Luis Mata Lomelí")
    print("Matricula: A01377205")
    print(" ")
    print("Menú principal")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Terminar")

    print(" ")
    opcion = int(input("Elige tu opción: "))
    print(" ")

    return opcion


#Funcion que recibe como parametro el dividendo y el divisor e imprime el cociente y el residuo

def dividir(dividendo, divisor):  #Restar el divisor tantas veces como sea del dividendo

#Contador y acumulador
    cosciente = 1
    residuo = 0

#Mientras la resta de del dividendo y divisor sea mayor o igual a 0...

    while dividendo - divisor >= residuo:

# Residuo = ultimo valor del cual ya no se puede restar más
        residuo = divisor * cosciente

#Cociente = numero de veces que se pudo restar el divisor del dividendo
        cosciente = cosciente + 1

#Imprimir los resultados...
    print(dividendo, "/", divisor, "=", cosciente - 1, ", y  sobra ", dividendo - residuo)


#Funcion para encontrar e imprimir el mayor de un conjunto de valores enteros positivos que teclee el usuario
def encontrarMayor():

#Contador y numeros dados ...
    mayor = 0
    numero_usuario = int(input("Teclea un numero [-1 para terminar de teclear]: "))

#Mientras el numero dado por el usuario no sea -1, hacer la condicion...
    while numero_usuario != -1:

#Si el numero de usuario es mayor a 0, es verdadero
        if numero_usuario > mayor:

# Al decir que mayor = numero_usuario, se creara un bucle donde mayor = numero_usuario mas grande
#Ejem: numero_usuario = 13 y, como 13 es mayor a 0, mayor es igual a 13. Luego el usuario pone 23 y como 23 es mayor a 13, ahora mayorr = 23
# pero, si el usuario pone ahora 3, 3 no es mayor a 23 por lo que mayor sigue siendo 13.

            mayor = numero_usuario

#Repetimos la peticion para poder aplicar correctamente el bucle

        numero_usuario = int(input("Teclea un numero [-1 para terminar de teclear]: "))

#Una vez el usuario ponga -1 en numero_usuario, el mayor debe imprimirse

    print("Mayor = ", mayor)


#Funcion Principal
def main():

    #Una vez guardada la opcion del usuario, aqui aplicamos las demas funciones segun su opinion.
    opcion = leerMenu()

    #Si el usuario escribe 3, el programa termina de manera automatica...
    #Mientras no pase esto...
    while opcion != 3:

        if opcion == 1:
            dividendo = int(input("Escribe el dividendo: "))
            divisor = int(input("Escribe el divisor: "))
            dividir(dividendo, divisor)

        if opcion == 2:
            encontrarMayor()

        opcion = leerMenu()

    print("Terminando programa...")
    print("Gracias")


main()