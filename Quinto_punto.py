'''
Imprimir el factorial de un número natural n dado.

'''
def factorialDeUnNumero(x:int) -> int:
    # Función que recibe un parametro y calcula el factorial del parametro recibido
    factorial = 1
    while(x >= 2):
        # Bucle que redefine el valor de factorial, decrementando en uno el parametro hasta que este sea menor a 2 y lo multiplica por la cantidad anteriormente guardada en factorial 
        factorial = x * factorial
        x -= 1 
    return factorial

if __name__ == "__main__":
    # Función Main que recibe un número natural y lo envía como parametro a la funcion factorialDeUnNumero y al final inprime el fatorial del número recibido
    x = int(input("Ingrese un número natural: "))
    factorial = factorialDeUnNumero(x)
    print (str(x)+ "! = " +str(factorial))