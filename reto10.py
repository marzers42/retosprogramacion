"""
/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */
"""

import requests

url =  'https://api.math.tools'

response = requests.get(url)

# Estado de la conexion con la API

if response:
    print("Response OK")
else:
    print("Resonse Failed")
    
# Imrprimir los header

print(response.headers)

# Texto Respuesta

print(response.text)