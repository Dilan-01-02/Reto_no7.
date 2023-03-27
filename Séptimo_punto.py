'''
Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

'''
bandera : bool = True

def divisores (x:int):
    # Función que imprime los números de un número recibido como parámetro
    i : float = 2.0 
    print("Los divisores del número "+str(x)+" son: ")
    while i <= (x/2):
        # Bucle que busca e imprime los divisores de un número
        if x%i == 0:
            print(i)
        i += 1

if __name__ == "__main__":
    # Función Main que le pide al usuario que ingrese un número que se encuentre en el rango se dos a cincuenta para conocer sus divisores
    # Y envía como parámetro el número ingresado a la función divisores
    while bandera or (x<2 or x>50):
        bandera = False
        x = int(input("Ingrese un número natural que se encuentre dentro de 2 y 50: "))
        if x<2 or x>50:
            print("El número ingresado no se encuentra en el rango solicitado")
    div = divisores(x)
    
    
