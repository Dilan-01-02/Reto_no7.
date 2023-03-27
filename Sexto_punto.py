'''
Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.

'''
import random
# Importación del módulo random para obetener un número al azar que se encuentre en el rango de 1 a 100

def adivinar(num:int):
    # Función para adivinar un número recibido como parametro, comparándolo con un número ingresado por el usuario y a su vez entregandole pistas
    bandera : bool = True
    i : int = 0
    while bandera or (x != num):
        # Bucle que recibe el número ingresado por el usuario y entrega pistas para adivinar el número definido por la funcion randint 
        bandera = False
        x = int(input("Ingrese un número del 1 al 100 para adivinar el número: "))
        if x < num:
            # Condición que le indica al usuario que el número a adivinar es mayor al número ingresado 
            print("El número es mayor a " +str(x))
        if x > num:
            # Condición que le indica al usuario que el número a adivinar es menor al número ingresado
            print("El número es menor a " +str(x))
        i += 1
        if i == 3:
            # Condición que después de tres intentos fallidos, le da al usuario pistas de si el número a adivinar es par o impar 
            if num % 2 == 0:
                # Condición que le indica al usuario que el número a adivinar es par 
                print("PISTA: El número es par\n")
            if num % 2 != 0:
                # Condición que le indica al usuario que el número a adivinar es impar
                print("\nPISTA: El número es impar\n")
    # Impresión del mensaje para cuando el usuario adivine el número
    print("\nENHORABUENA: Usted adivinó el número")

if __name__ == "__main__":
    # Función main que define el número al azar entre el rango de 1 a 100 y lo envía como parámetro a la función adivinar
    num = random.randint(1,100)
    numero = adivinar(num)