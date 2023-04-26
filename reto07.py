"""
/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
"""

"""
gryffindor: valor
hufflepuff: lealtad
revenclaw: sabiduria
Slythering: ambicion
"""

class HatQuestion:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

def get_answer():

    answer = input("Responde 1, 2 ,3 o 4: ")
    if answer == "1" or answer == "2" or answer == "3" or answer == "4":
        return int(answer)
    return get_answer()

print("Hola soy el \"sombrero seleccionador\"\n Tendras que responder cinco preguntas para ayudarme a descubrir tu casa de Howarts.\n")

hat_questions = [HatQuestion("¿Como te definirias?", [
    ("1. Valiente", "gryffindor"),
    ("2. Leal","hufflepuff"),
    ("3. Sabio","revenclaw"),
    ("4. Ambicioso","slytherin")]),
    HatQuestion("¿Cual es tu clase favorita?", [
    ("1. Vuelo","gryffindor"),
    ("2. Pociones","revenclaw"),
    ("3. Defensa contra las artes oscuras","slytherin"),
    ("4. Animales Fantasticos","hufflepuff")]),
    HatQuestion("¿Donde Pasarias el tiempo?", [
    ("1. Invernadero","hufflepuff"),
    ("2. Biblioteca","revenclaw"),
    ("3. En la sala comun","slytherin"),
    ("4. Explorando","gryffindor")]),
    HatQuestion("¿Cual es tu colo favorito=", [
    ("1. Rojo ","gryffindor"),
    ("2. Azul","revenclaw"),
    ("3. Verde","slythyerin"),
    ("4. Amarillo","hufflepuff")]),
    HatQuestion("¿Cual es tu mascota?", [
    ("1. Sapo","revenclaw"),
    ("2. Lechuza","gryffindor"),
    ("3. Gato","hufflepuff"),
    ("4. Sepriente","slytherin")])]

houses = {
    "gryffindor": 0,
    "hufflepuff": 0,
    "revenclaw": 0, 
    "slytherin": 0
}

for hat_question in hat_questions:
    print(hat_question.question)
    for hat_answers in hat_question.answers:
        print(hat_answers[0])

    house = hat_question.answers[get_answer() - 1][1]
    houses[house] += 1

    print()

selected_house = []
max_points = 0

for house, points in houses.items():
    if points > max_points:
        selected_house.clear()
        selected_house.append(house)
        max_points = points
    elif points == max_points:
        selected_house.append(house)
        max_points = points

if len(selected_house) == 1:
    print(f"Lo tengo claro... ¡{selected_house[0].capitalize()}!")
else:
    print(f"Ha estado complicado... ¡{random.choice(selected_house).capitalize()}!")


