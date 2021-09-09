"""
Fecha de creación: 09/sep/21
Autor: Cristopher Olivares 
"""
lista = [4,5,6,7,5,45,5,8,5]
contenidoLista = len(lista)

print ('La siguiente lista:',lista, 'tiene un total de', contenidoLista, 'elementos.')

a = contenidoLista % 2
c = contenidoLista / 2

if a == 0:
    d = lista [int(c)]
    lista.remove (d)
    print('Valor de elemetos de lista par, eliminaremos el elemento previo al punto medio:')
    print (lista)
else:
    d = lista [int(c)]
    lista.remove(d)
    print('Valor de elementos de lista impar, eliminaremos el elemento medio:')
    print (lista)
    
    
