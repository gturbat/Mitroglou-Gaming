import move_2048

def set_direction(grid, tour):
    dic_move = {0: "g", 1: "d", 2: "h", 3: "b"}
    moves = move_2048.move_possible(grid)
    commands_possible = [dic_move[i] for i in range(4) if moves[i]]
    compteur_ia = tour % 3
    if dic_move[compteur_ia+1] in commands_possible:
        return dic_move[compteur_ia+1]
    elif 'g' in commands_possible:
        return 'g'
    else:
        return commands_possible[0]


def set_size_grid():
    size=""
    while not size.isdigit():
        size = input("Entrez la taille de la grille")
    return size


def set_theme_grid():
    theme=""
    while not theme in ["0","1","2"]:
        theme = input ("Entrez le numero du theme")
    return theme
