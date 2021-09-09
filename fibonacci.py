"""
Fecha de creación: 09/sep/21
Autor: Cristopher Olivares 
"""
def fibonacci (n):
    if n == 0:
        return  0
    elif n == 1:
        return  1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
x = 7
resultado = fibonacci(x)
print (f'En la serie de Fibonacci el lugar {x} tiene como resultado {resultado}')


#Extra: opción para que el usuario elija el lugar que quiera
y = int (input ('Elige un lugar en la serie de fibonacci'))
respuesta = fibonacci (y)
print (f'En la serie de Fibonacci el lugar {y} tiene como resultado {respuesta}')