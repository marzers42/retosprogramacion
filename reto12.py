"""
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
"""

import datetime

def friday_13(year:int, month:int) -> bool:
    return datetime.date(year, month, 13).weekday() == 4.

print(friday_13(2023, 1))


