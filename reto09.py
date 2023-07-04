""" 
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
"""
def heterograma(palabra):
    dic_hetero = []
    for letra in palabra:
        dic_hetero.append(letra)
    for j in dic_hetero:
        if dic_hetero.count(j) > 1:
            print("La palabra no es heterograma")
            break
        else:
            print("La palabra es heterograma")
    
    """for j in range(0, len(dic_hetero)):
        if dic_hetero[j] == dic_hetero[j+1]:
            print("No es heterograma")
            break                
        else:
            print("Es heterograma")
    """



def isograma(palabra):
    
    return

def pangrama(palabra):
    
    return
"""
#### Solucion de Mouv

import re
import unicode

def dicc_palabra(text: str) -> dict[str, int]:
    char_counter= dict()
    for char in text:
        if char in char_counter.keys():
            char_counter[char] += 1
        else:
            char_counter = 1
"""



primerapalabra = "eaiou"

heterograma(primerapalabra)




