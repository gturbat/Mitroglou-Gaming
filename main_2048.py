import grid_2048
import move_2048

def play(ia):
    if not ia:
        import textual_2048
        dic_move = {0: "g", 1: "d", 2: "h", 3: "b"}
        size = int(textual_2048.set_size_grid())
        theme = grid_2048.py.THEMES[textual_2048.set_theme_grid()]
        grid = grid_2048.py.init_game(size)
        print("Situation de départ :")
        print(grid_2048.py.grid_to_string_with_size_and_theme(grid, theme, size))
        tour = 1
        while not move_2048.is_game_over(grid) and grid_2048.py.get_grid_tile_max(grid) < 2048:
            moves = move_2048.move_possible(grid)
            commands_possible = [dic_move[i] for i in range(4) if moves[i]]
            command = textual_2048.set_direction()
            while not command in commands_possible:
                print("Deplacement impossible")
                command = textual_2048.set_direction()
            grid = move_2048.move_grid(grid, command)
            if not grid_2048.py.is_full_grid(grid):
                grid = grid_2048.py.grid_add_new_tile(grid)
            print("Tour {}, deplacement {} :".format(tour, command))
            print(grid_2048.py.grid_to_string_with_size_and_theme(grid, theme, size))
            tour += 1
        if grid_2048.py.get_grid_tile_max(grid) >= 2048:
            return "Victoire !"
        return "Game Over"
    else:
        import ia_2048
        dic_move = {0: "g", 1: "d", 2: "h", 3: "b"}
        size = int(ia_2048.set_size_grid())
        theme = grid_2048.py.THEMES[ia_2048.set_theme_grid()]
        grid = grid_2048.py.init_game(size)
        print("Situation de départ :")
        print(grid_2048.py.grid_to_string_with_size_and_theme(grid, theme, size))
        tour = 1
        while not move_2048.is_game_over(grid) and grid_2048.py.get_grid_tile_max(grid) < 2048:
            moves = move_2048.move_possible(grid)
            commands_possible = [dic_move[i] for i in range(4) if moves[i]]
            command = ia_2048.set_direction()
            while not command in commands_possible:
                print("Deplacement impossible")
                command = ia_2048.set_direction()
            grid = move_2048.move_grid(grid, command)
            if not grid_2048.py.is_full_grid(grid):
                grid = grid_2048.py.grid_add_new_tile(grid)
            print("Tour {}, deplacement {} :".format(tour, command))
            print(grid_2048.py.grid_to_string_with_size_and_theme(grid, theme, size))
            tour += 1
        if grid_2048.py.get_grid_tile_max(grid) >= 2048:
            return "Victoire !"
        return "Game Over"
