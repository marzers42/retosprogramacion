#/*
# * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# * Podrás configurar generar contraseñas con los siguientes parámetros:
# * - Longitud: Entre 8 y 16.
# * - Con o sin letras mayúsculas.
# * - Con o sin números.
# * - Con o sin símbolos.
# * (Pudiendo combinar todos estos parámetros entre ellos)
#*/

# Librerias que vamos a ocupar

from random import choice 
import math

letras_min = 'abcdefghijklmnopqrstuvwxyz'
letas_mayus = letras_min.upper()
numeros = '1234567890'
especiales = '!@#$%&/()=?*¨[]'

# NOTA: el join nos permite hacer los elementos de una lista en una cadena

#alfabeto = letras_min + letas_mayus + numeros + especiales
#longitud = int(input('Que longitud es tu pass'))
#pas = ''
#pas = pas.join([choice(alfabeto) for i in range(longitud)])
#contrasena = pas
#print(contrasena)

# Ya hecha la contraseña que es general vamos a hacer una contraseña que cumpla las reglas

alfabeto = letras_min + letas_mayus + numeros + especiales


longitud = int(input('Que longitud es tu pass?'))
maysuculas = int(input('Que tenga mayusculas?'))
signos = int(input('Que tenga signos?'))
num = int(input('Que tenga numeros?'))
pas = ''

print(longitud)
print(maysuculas)
print(signos)
print(num)


if maysuculas == 1:
    print("este print si sirve LOL")


if maysuculas == 1:
    alfabeto = letras_min + letas_mayus + especiales + numeros
    pas = pas.join([choice(alfabeto) for i in range(longitud)])
    print("opcion 1")
    contrasena = pas
    print(pas)
if maysuculas == 0 and signos == 1 and numeros == 1:
    alfabeto = letras_min + numeros + especiales
    pas = pas.join([choice(alfabeto) for i in range(longitud)])
    contrasena = pas
    print(contrasena)
if maysuculas == 0 and signos == 0 and numeros == 1:
    alfabeto = letras_min + numeros
    pas = pas.join([choice(alfabeto) for i in range(longitud)])
    contrasena = pas
    print(contrasena)
if maysuculas == 0 and signos == 0 and numeros == 0:
    alfabeto = letras_min
    pas = pas.join([choice(alfabeto) for i in range(longitud)])
    contrasena = pas
    print(contrasena)
if maysuculas == 1 and signos == 0 and numeros == 0:
    alfabeto = letras_min + letas_mayus
    pas = pas.join([choice(alfabeto) for i in range(longitud)])
    contrasena = pas
    print(contrasena)
if maysuculas == 1 and signos == 1 and numeros == 0:
    alfabeto = letras_min + letas_mayus + signos
    pas = pas.join([choice(alfabeto) for i in range(longitud)])
    contrasena = pas
    print(contrasena)
