"""
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

"""

"""
Indicqciones:

Spock > tijera > lagarto
tijer > papel > spock
papel > piedra > tijera
piedra > lagarto > papel
lagarto > spock > tijera
spock > piedra 
"""
    

def piedra_tijera_spock_lagarto_papel(games):
    
    rules = {"rock": ["lagarto","tijera"],
             "tijera":["lagarto","papel"],
             "papel":["rock","spock"],
             "lagarto":["spock","papel"],
             "spock":["rock","tijera"]}
    
    player_one = 0
    player_two = 0

    for game in games:
        player_one_game = game[0]
        player_two_game = game[1]
        if player_one_game != player_two_game:
            if player_two_game in rules[player_one_game]:
                player_one += 1
            else:
                player_two += 1

    return "Tie" if player_one == player_two else "Player 1" if player_one > player_two else "Player 2"



print(piedra_tijera_spock_lagarto_papel([("rock","tijera")]))


"""Como funciona?
Metemos una lista a nuestra funcion
En la parte de los if, hacemos buscando en el diccionario nos diga si cae en la matriz
La idea proncipal esta en la contruccion de la matriz, es bueno hacerlo comom un diccionario 
"""