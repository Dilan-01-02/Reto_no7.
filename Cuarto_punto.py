'''
En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18,9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. 
Desarrollar un algoritmo para informar en que año la población del país B superará a la de A

'''
A = 25
B = 18.9
i : int = 2022

while (B <= A):
    # Este bucle incrementa la población de cada país por su tasa de creciemiento poblacional anual e incrementa en uno, los años transcurridos cada vez que se realiza un incremento, hasta que la población del país B sea mayor a la del país A.
    A = A * (1 + 0.02)
    B = B * (1 + 0.03)
    i += 1

print("En el año " +str(i)+ " el país B superará la población del país A")