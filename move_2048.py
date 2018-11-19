import copy


def move_row_left(row):
    new_row = copy.copy(row)
    for y in range(len(new_row)):
        if new_row[y]==0 :
            new_row[y] = " "
    limite=0
    for y in range(1, len(new_row)):
        if new_row[y] != 0:
            while y > 0 and new_row[y - 1] == " " :
                new_row[y - 1], new_row[y] = new_row[y], " "
                y -= 1
            if y > limite and new_row[y - 1] == new_row[y]:
                new_row[y - 1], new_row[y] = 2 * new_row[y - 1], " "
                limite=y
    return new_row

def move_row_right(row):
    new_row = copy.copy(row)
    new_row.reverse()
    new_row = move_row_left(new_row)
    new_row.reverse()
    return new_row


def move_grid(grid, d):
    new_grid = copy.deepcopy(grid)
    if d == "g":
        for x in range(len(new_grid)):
            new_grid[x] = move_row_left(new_grid[x])
    elif d == "d":
        for x in range(len(new_grid)):
            new_grid[x] = move_row_right(new_grid[x])
    elif d == "h":
        for y in range(len(new_grid[0])):
            column = [x[y] for x in grid]
            column = move_row_left(column)
            for x in range(len(column)):
                new_grid[x][y] = column[x]
    elif d == "b":
        for y in range(len(new_grid[0])):
            column = [x[y] for x in grid]
            column = move_row_right(column)
            for x in range(len(column)):
                new_grid[x][y] = column[x]
    return new_grid


def move_possible(grid):
    size = len(grid)
    """
    return boolean for moving in [left, right, up, down] 
    """
    moves = [False, False, False, False]
    find = False
    for x in range(size):
        if find:
            break
        for y in range(1, size):
            if grid[x][y] not in [0, " "] and (grid[x][y - 1] in [grid[x][y], 0, " "]):
                moves[0] = True
                find = True
                break
    find = False
    for x in range(size):
        if find:
            break
        for y in range(size - 2, -1, -1):
            if grid[x][y] not in [0, " "] and (grid[x][y + 1] in [grid[x][y], 0, " "]):
                moves[1] = True
                find = True
                break
    find = False
    for y in range(size):
        if find:
            break
        for x in range(1, size):
            if grid[x][y] not in [0, " "] and (grid[x - 1][y] in [grid[x][y], 0, " "]):
                moves[2] = True
                find = True
                break
    find = False
    for y in range(size):
        if find:
            break
        for x in range(size - 2, -1, -1):
            if grid[x][y] not in [0, " "] and (grid[x + 1][y] in [grid[x][y], 0, " "]):
                moves[3] = True
                find = True
                break
    return moves

def is_game_over(grid):
    if True in move_possible(grid):
        return False
    return True
