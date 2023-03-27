'''
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

'''
def paresDescendentes(i:int):
    # Esta función convierte los impares a pares e imprime los pares mayores a dos
    if (i % 2 !=0):
        # Este condicional convierte un posible número impar recibido, a un número par restandole uno
        i = i - 1
        
    while(i >= 2):
        # Este bucle imprime los números impares siempre y cuando estos sean mayores a dos 
        print(" --> " +str(i))
        i -= 2

if __name__ == "__main__":
    # Función Main que recibe un número natural mayor o igual a dos y envia este número como parametro a la funcion paresDescendentes
    i = int(input("Ingrese un número natural mayor o igual a dos: "))
    par = paresDescendentes(i)


