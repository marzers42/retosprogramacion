"""
/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */
"""

def ladder(step:int):
    if step > 0 :
        for i in range(step-1,-1,-1):
            print(i*" "+"_|")
    elif step < 0:
        step = step*-1
        #print("Es negativa")
        for i in range(step):
            print(i*" "+"|_")
    else:
        print("__")


ladder(0)
ladder(5)
ladder(-5)
