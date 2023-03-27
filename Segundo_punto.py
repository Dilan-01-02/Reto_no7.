'''
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

'''
i : int = 0
print("IMPARES")
while (i<=499):
    # Este bucle imprime los números impares del 1 al 999
    print(2 * i + 1)
    i += 1
print("\n")

i = 1
print("PARES")
while (i<=500):
    # Este bucle imprime los números pares del 2 al 1000
    print(2*i)
    i += 1