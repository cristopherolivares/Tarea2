"""
Fecha de creación: 09/sep/21
Autor: Cristopher Olivares 
"""

#incompleto
def conteo(c):
    if c == 0 :
        return 0
    else:
        return conteo(c-1)

x = 5
resultado = conteo(x)
print (f'{resultado}')