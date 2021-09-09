"""
Fecha de creación: 09/sep/21
Autor: Cristopher Olivares 
"""

#incompleto
def lista(l):
    a = len(l)
    if a == 0 :
        return 0
    else:
        return lista(l - 1) + lista(l - 2)
        
x = [2,3,5,6]

resultado = lista(x)

print (f'  {x}  {resultado}')
