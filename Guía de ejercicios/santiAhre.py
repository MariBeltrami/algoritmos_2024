from pila import Stack

def find_positions(stack, names):
    temp_stack = Stack()
    positions = {}
    position = 1

    while stack.size() > 0:
        character = stack.pop()
        temp_stack.push(character)
        if character["name"] in names:
            positions[character["name"]] = position
        position += 1

    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())

    return positions
def more_than_five_movies(stack):
    temp_stack = Stack()
    result = []

    while stack.size() > 0:
        character = stack.pop()
        temp_stack.push(character)
        if character["movies"] > 5:
            result.append((character["name"], character["movies"]))

    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())

    return result
def black_widow_movies(stack):
    temp_stack = Stack()
    black_widow_count = 0

    while stack.size() > 0:
        character = stack.pop()
        temp_stack.push(character)
        if character["name"] == "Black Widow":
            black_widow_count = character["movies"]

    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())

    return black_widow_count
def characters_starting_with(stack, initials):
    temp_stack = Stack()
    result = []

    while stack.size() > 0:
        character = stack.pop()
        temp_stack.push(character)
        if character["name"][0] in initials:
            result.append(character["name"])

    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())

    return result
mcu_stack = Stack()
mcu_stack.push({"name": "Iron Man", "movies": 10})
mcu_stack.push({"name": "Captain America", "movies": 9})
mcu_stack.push({"name": "Rocket Raccoon", "movies": 5})
mcu_stack.push({"name": "Groot", "movies": 4})
mcu_stack.push({"name": "Black Widow", "movies": 7})
mcu_stack.push({"name": "Doctor Strange", "movies": 3})

# a. Determinar en qué posición se encuentran Rocket Raccoon y Groot
positions = find_positions(mcu_stack, ["Rocket Raccoon", "Groot"])
print("Posiciones:", positions)

# b. Determinar los personajes que participaron en más de 5 películas
more_than_five = more_than_five_movies(mcu_stack)
print("Personajes en más de 5 películas:", more_than_five)

# c. Determinar en cuántas películas participó Black Widow
black_widow_count = black_widow_movies(mcu_stack)
print("Black Widow participó en", black_widow_count, "películas")

# d. Mostrar todos los personajes cuyos nombres empiezan con C, D y G
characters_cd_g = characters_starting_with(mcu_stack, {'C', 'D', 'G'})
print("Personajes que empiezan con C, D, G:", characters_cd_g)