import random
import copy

THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256",
                512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"},
          "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O",
                512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"},
          "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H",
                512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


def create_grid(size):
    game_grid = []
    for i in range(size):
        game_grid.append([' ' for k in range(size)])
    return game_grid


def get_all_tiles(grid):
    tiles = []
    for x in grid:
        for xy in x:
            if xy == " ":
                tiles.append(0)
            else:
                tiles.append(xy)
    return tiles


def get_value_new_tile():
    return random.choices([2, 4], [0.9, 0.1])[0]


def get_empty_tiles_positions(grid):
    empty_tiles = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] in [" ", 0]:
                empty_tiles.append((x, y))
    return empty_tiles


def get_new_position(grid):
    xy = random.choices(get_empty_tiles_positions(grid))[0]
    return xy[0], xy[1]


def grid_get_value(grid, x, y):
    if grid[x][y] == " ":
        return 0
    return grid[x][y]


def grid_add_new_tile(grid):
    x, y = get_new_position(grid)
    new_grid = copy.deepcopy(grid)
    new_grid[x][y] = get_value_new_tile()
    return new_grid


def init_game(size):
    grid = create_grid(size)
    grid = grid_add_new_tile(grid)
    grid = grid_add_new_tile(grid)
    return grid


def grid_to_string(grid):
    affichage = ""
    barre = " ===" * len(grid[0])
    barre += "\n"
    for x in grid:
        affichage += barre
        for xy in x:
            if xy in [" ", 0]:
                affichage += "| 0 "
            else:
                if xy < 10:
                    affichage += "| {} ".format(xy)
                elif xy < 100:
                    affichage += "|{} ".format(xy)
                else:
                    affichage += "|{}".format(xy)
        affichage += "|\n"
    affichage += barre
    return affichage


def grid_to_string_with_size(grid, size):
    if long_value(grid) <= 3:
        return grid_to_string(grid)
    else:
        affichage = ""
        barre = " ====" * len(grid[0])
        barre += "\n"
        for x in grid:
            affichage += barre
            for xy in x:
                if xy in [" ", 0]:
                    affichage += "| 0  "
                else:
                    if xy < 10:
                        affichage += "| {}  ".format(xy)
                    elif xy < 100:
                        affichage += "| {} ".format(xy)
                    elif xy < 1000:
                        affichage += "|{} ".format(xy)
                    else:
                        affichage += "|{}".format(xy)
            affichage += "|\n"
        affichage += barre
        return affichage


def long_value(grid):
    length = 0
    for x in grid:
        for xy in x:
            if xy in [0, " "]:
                if length < 1:
                    length = 1
            elif length < len(str(xy)):
                length = len(str(xy))
    return length


def long_value_with_theme(grid, theme):
    length = 0
    for x in grid:
        for xy in x:
            if xy in [0, " "]:
                if len(theme[0]) > length:
                    length = len(theme[0])
            elif len(theme[xy]) > length:
                length = len(theme[xy])
    return length


def grid_to_string_with_size_and_theme(grid, theme, size):
    m = long_value_with_theme(grid, theme)
    affichage = ""
    barre = (" " + "=" * m) * len(grid[0])
    barre += "\n"
    for x in grid:
        affichage += barre
        for xy in x:
            if xy in [" ", ""]:
                xy = 0
            length_tile = len(theme[xy])
            if (m - length_tile) % 2 == 0:
                affichage += "|" + " " * ((m - length_tile) // 2) + theme[xy] + " " * ((m - length_tile) // 2)
            else:
                affichage += "|" + " " * ((m - length_tile) // 2) + theme[xy] + " " * ((m - length_tile) // 2 + 1)
        affichage += "|\n"
    affichage += barre
    return affichage


def is_full_grid(grid):
    for x in grid:
        for xy in x:
            if xy in [0, " ", ""]:
                return False
    return True


def get_grid_tile_max(grid):
    max = 0
    for x in grid:
        for xy in x:
            if xy != " " and xy > max:
                max = xy
    return max
