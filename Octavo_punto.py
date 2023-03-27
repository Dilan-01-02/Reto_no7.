'''
Implementar el algoritmo que muestre los números primos del 1 al 100. nota: use funciones

'''
def numPrimo (x:int) -> bool:
    # Función que determina si el número recibido como parámetro es un número primo o no lo es
    i : int = 2
    bandera : bool = True
    while bandera and (i <= x**0.5):
        # Bucle que busca al menos un divisor del número recibido como parámetro para determinar si este es primo o no
        if x % i == 0:
            bandera = False
        i += 1
    return bandera

if __name__ == "__main__":
    # Funcion maín que imprime los números primos desde 1 hasta 100 
    x : int = 1
    while (x>=1 and x<=100):
        num = numPrimo(x)
        if num == True:
            print(x)
        x += 1