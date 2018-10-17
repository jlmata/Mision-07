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

#Cociente = numero de veces que se pudo restar el divisor del dividendo
#Residuo = ultimo valor del cual ya no se puede restar más

def dividir(dividendo, divisor):  #Restar el divisor tantas veces como sea del dividendo

    cosciente = 1
    residuo = 0

    while dividendo - divisor >= residuo:
        residuo = divisor * cosciente
        cosciente = cosciente + 1

    print(dividendo, "/", divisor, "=", cosciente - 1, ", y  sobra ", dividendo - residuo)


#Funcion para encontrar e imprimir el mayor de un conjunto de valores enteros positivos que teclee el usuario
def encontrarMayor():

    mayor = 0
    suma = 0

    numero_usuario = int(input("Teclea un numero [-1 para terminar de teclear]: "))

    while numero_usuario != -1:

        suma += numero_usuario

        if numero_usuario > mayor:
            mayor = numero_usuario

        numero_usuario = int(input("Teclea un numero [-1 para terminar de teclear]: "))

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