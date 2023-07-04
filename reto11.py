"""
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
"""

def analizer_url(url):  
    url_par1 = url.find("?")
    url_par2 = url.find("&")
    print(url[url_par1+1:url_par2])
    print(url[url_par2+1:])
        
            
                        

reto_url = "https://retosdeprogramacion.com?year=2023&challenge=0"

analizer_url(reto_url)
