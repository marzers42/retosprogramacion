"""

 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...

"""

"""
Consideraciones: 
    - la semilla debera ser mayor a 4 digitos
    - Si el resultado tiene menos de 4 digitos se añadiran ceros al incio
"""
#import math


def mid_sqrt(seed):
    seed_str = str(seed)
    seed_int = int(seed)
    if len(seed_str) < 8:
        sedd_str = seed_str + "000"
        seed_int =int(sedd_str)
        value = seed_int**2
    else:
        value = seed_int**2
    value_str = str(value)
    resultado = int(value_str[3:9])%100
    print(resultado)    


prueba = mid_sqrt(75894)
