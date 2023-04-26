"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""

"""
* ¿Que es un numero de fibonacci?
* ¿Que es un numero par?
* ¿Que es un numero primo?
"""
def num_primos(primos):
    restotal = []
    for primo in range(0, int(primos)):
        res = primos % (primo + 1)
        restotal.append((res))
    if restotal.count(0) > 2:
        print("No es un primo")
    else:
        print("es un primo")
            

def num_fibonacci(fibo):
    number1 = 0 
    number2 = 1
    contar = 0
    acumuladalist = []
    while contar < fibo:
        acumulada = number1 + number2
        acumuladalist.append(acumulada)
        number1 = number2
        number2 = acumulada
        contar += 1
    #print(acumuladalist)
    for i in acumuladalist:
        if i == fibo:
            print("Es numero de fibonacci")
            break
        else:
            print("No es numero de fibonacci")
    
def numelizer(numero):
    int(numero)
    if numero % 2 == 0:
        print("Es multiplo de 2")
    else:
        print("No es multiplo de 2")


numelizer(25)

num_primos(25)

num_fibonacci(3)