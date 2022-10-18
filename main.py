import random
import tkinter as tk
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import copy

def main():
    start_fenster()
    game_fenster_update()
    window.mainloop()

def rng(height, width):
    random_height_coordinate = random.randint(1, height)
    random_width_coordinate = random.randint(1, width)
    return random_height_coordinate, random_width_coordinate

def start_fenster():
    window.geometry("512x512")
    start_button_creator()
    quit_button_creator()

def handle_keypress(event):
    print(event.char)
    greeting = tk.Label(text=event.char)
    greeting.pack()

def quit_button_creator():
    # noinspection PyGlobalUndefined
    global quit_button
    quit_button = tk.Button(text="Quit", background="red")
    quit_button.bind("<Button-1>", handle_click_quit)
    quit_button.pack()

def handle_click_quit(event):
    window.quit()

# noinspection PyGlobalUndefined
def start_button_creator():
    global start_button
    start_button = tk.Button(text="Click me!", background="turquoise")
    start_button.bind("<Button-1>", handle_click_start)
    start_button.pack()
    global game_beatable
    game_beatable = 0
    global tile_type_save
    tile_type_save = 1

def handle_click_start(event):
    start_button.destroy()
    quit_button.destroy()
    play()

# noinspection PyGlobalUndefined
def play():
    global game_beatable
    game_beatable = 0
    while game_beatable == 0:
        tile_type_creator()
        check_game_beatable()
    game_frame_creator()

def game_fenster():
    greeting = tk.Label(text="Daniel ist ein netter Mensch")
    greeting.pack()

def game_frame_creator():
    window.geometry("512x512")
    #screen_height_setting = 5
    #screen_width_setting = 5

    for screen_height in range(map_height + 3):
        window.rowconfigure(screen_height, minsize=64)
        for screen_width in range(map_width):
            window.columnconfigure(screen_width, minsize=64)
            # noinspection PyGlobalUndefined
            #global frame_game
            frame_game = tk.Frame(master=window)
            frame_game.grid(row=screen_height, column=screen_width)
            #tile_label = tk.Label(master=frame_game, text=f"Row {screen_height}\nColumn {screen_width}")
            #tile_label.grid()
            tile_updater()

    button_up = tk.Button(master=window, bg="beige", text="↑")
    button_down = tk.Button(master=window, bg="beige", text="↓")
    button_left = tk.Button(master=window, bg="beige", text="←")
    button_right = tk.Button(master=window, bg="beige", text="→")
    button_interact = tk.Button(master=window, bg="beige", text="use")
    button_quit = tk.Button(master=window, bg="beige", text="Quit")
    button_restart = tk.Button(master=window, bg="beige", text="Restart")

    button_up.bind("<Button-1>", handle_click_up)
    button_down.bind("<Button-1>", handle_click_down)
    button_left.bind("<Button-1>", handle_click_left)
    button_right.bind("<Button-1>", handle_click_right)
    #button_interact.bind("<Button-1>", handle_click_interact)
    button_quit.bind("<Button-1>", handle_click_quit)
    button_restart.bind("<Button-1>", handle_click_start)

    button_up.grid(row=5, column=1, sticky="nesw")
    button_down.grid(row=7, column=1, sticky="nesw")
    button_left.grid(row=6, column=0, sticky="nesw")
    button_right.grid(row=6, column=2, sticky="nesw")
    button_interact.grid(row=6, column=1, sticky="nesw")
    button_quit.grid(row=7, column=4, sticky="nesw")
    button_restart.grid(row=6, column=4, sticky="nesw")

# noinspection PyGlobalUndefined
def handle_click_up(event):
    player_height_coordinate, player_width_coordinate = search_tile_state(2)
    global tile_type_save
    global matrix

    if player_height_coordinate - 1 < 0:
        print("walk error map border")
    else:
        if matrix[player_height_coordinate - 1][player_width_coordinate] == 0:
            print("walk error tree")
        else:
            if matrix[player_height_coordinate - 1][player_width_coordinate] == 5:
                print("dead")
            else:
                tile_type_save_new = matrix[player_height_coordinate - 1][player_width_coordinate]
                matrix[player_height_coordinate - 1][player_width_coordinate] = 2
                matrix[player_height_coordinate][player_width_coordinate] = tile_type_save
                tile_type_save = tile_type_save_new

    tile_updater()

# noinspection PyGlobalUndefined
def handle_click_down(event):
    player_height_coordinate, player_width_coordinate = search_tile_state(2)
    global tile_type_save
    global matrix

    if player_height_coordinate + 1 > map_height - 1:
        print("walk error map border")
    else:
        if matrix[player_height_coordinate + 1][player_width_coordinate] == 0:
            print("walk error tree")
        else:
            if matrix[player_height_coordinate + 1][player_width_coordinate] == 5:
                print("dead")
            else:
                tile_type_save_new = matrix[player_height_coordinate + 1][player_width_coordinate]
                matrix[player_height_coordinate + 1][player_width_coordinate] = 2
                matrix[player_height_coordinate][player_width_coordinate] = tile_type_save
                tile_type_save = tile_type_save_new

    tile_updater()

# noinspection PyGlobalUndefined
def handle_click_left(event):
    player_height_coordinate, player_width_coordinate = search_tile_state(2)
    global tile_type_save
    global matrix

    if player_width_coordinate - 1 < 0:
        print("walk error map border")
    else:
        if matrix[player_height_coordinate][player_width_coordinate - 1] == 0:
            print("walk error tree")
        else:
            if matrix[player_height_coordinate][player_width_coordinate - 1] == 5:
                print("dead")
            else:
                tile_type_save_new = matrix[player_height_coordinate][player_width_coordinate - 1]
                matrix[player_height_coordinate][player_width_coordinate - 1] = 2
                matrix[player_height_coordinate][player_width_coordinate] = tile_type_save
                tile_type_save = tile_type_save_new

    tile_updater()

# noinspection PyGlobalUndefined
def handle_click_right(event):
    player_height_coordinate, player_width_coordinate = search_tile_state(2)
    global tile_type_save
    global matrix

    if player_width_coordinate + 1 > map_width - 1:
        print("walk error map border")
    else:
        if matrix[player_height_coordinate][player_width_coordinate + 1] == 0:
            print("walk error tree")
        else:
            if matrix[player_height_coordinate][player_width_coordinate + 1] == 5:
                print("dead")
            else:
                tile_type_save_new = matrix[player_height_coordinate][player_width_coordinate + 1]
                matrix[player_height_coordinate][player_width_coordinate + 1] = 2
                matrix[player_height_coordinate][player_width_coordinate] = tile_type_save
                tile_type_save = tile_type_save_new

    tile_updater()

def game_fenster_update():
    print("yes")

def tile_updater():
    tile_type_0_0 = get_tile_type(0, 0)
    tile_type_0_1 = get_tile_type(0, 1)
    tile_type_0_2 = get_tile_type(0, 2)
    tile_type_0_3 = get_tile_type(0, 3)
    tile_type_0_4 = get_tile_type(0, 4)

    tile_type_1_0 = get_tile_type(1, 0)
    tile_type_1_1 = get_tile_type(1, 1)
    tile_type_1_2 = get_tile_type(1, 2)
    tile_type_1_3 = get_tile_type(1, 3)
    tile_type_1_4 = get_tile_type(1, 4)

    tile_type_2_0 = get_tile_type(2, 0)
    tile_type_2_1 = get_tile_type(2, 1)
    tile_type_2_2 = get_tile_type(2, 2)
    tile_type_2_3 = get_tile_type(2, 3)
    tile_type_2_4 = get_tile_type(2, 4)

    tile_type_3_0 = get_tile_type(3, 0)
    tile_type_3_1 = get_tile_type(3, 1)
    tile_type_3_2 = get_tile_type(3, 2)
    tile_type_3_3 = get_tile_type(3, 3)
    tile_type_3_4 = get_tile_type(3, 4)

    tile_type_4_0 = get_tile_type(4, 0)
    tile_type_4_1 = get_tile_type(4, 1)
    tile_type_4_2 = get_tile_type(4, 2)
    tile_type_4_3 = get_tile_type(4, 3)
    tile_type_4_4 = get_tile_type(4, 4)

    tile_0_0 = tk.Label(master=window, bg=tile_type_0_0)
    tile_0_1 = tk.Label(master=window, bg=tile_type_0_1)
    tile_0_2 = tk.Label(master=window, bg=tile_type_0_2)
    tile_0_3 = tk.Label(master=window, bg=tile_type_0_3)
    tile_0_4 = tk.Label(master=window, bg=tile_type_0_4)

    tile_1_0 = tk.Label(master=window, bg=tile_type_1_0)
    tile_1_1 = tk.Label(master=window, bg=tile_type_1_1)
    tile_1_2 = tk.Label(master=window, bg=tile_type_1_2)
    tile_1_3 = tk.Label(master=window, bg=tile_type_1_3)
    tile_1_4 = tk.Label(master=window, bg=tile_type_1_4)

    tile_2_0 = tk.Label(master=window, bg=tile_type_2_0)
    tile_2_1 = tk.Label(master=window, bg=tile_type_2_1)
    tile_2_2 = tk.Label(master=window, bg=tile_type_2_2)
    tile_2_3 = tk.Label(master=window, bg=tile_type_2_3)
    tile_2_4 = tk.Label(master=window, bg=tile_type_2_4)

    tile_3_0 = tk.Label(master=window, bg=tile_type_3_0)
    tile_3_1 = tk.Label(master=window, bg=tile_type_3_1)
    tile_3_2 = tk.Label(master=window, bg=tile_type_3_2)
    tile_3_3 = tk.Label(master=window, bg=tile_type_3_3)
    tile_3_4 = tk.Label(master=window, bg=tile_type_3_4)

    tile_4_0 = tk.Label(master=window, bg=tile_type_4_0)
    tile_4_1 = tk.Label(master=window, bg=tile_type_4_1)
    tile_4_2 = tk.Label(master=window, bg=tile_type_4_2)
    tile_4_3 = tk.Label(master=window, bg=tile_type_4_3)
    tile_4_4 = tk.Label(master=window, bg=tile_type_4_4)

    tile_0_0.grid(row=0, column=0, sticky="nesw")
    tile_0_1.grid(row=0, column=1, sticky="nesw")
    tile_0_2.grid(row=0, column=2, sticky="nesw")
    tile_0_3.grid(row=0, column=3, sticky="nesw")
    tile_0_4.grid(row=0, column=4, sticky="nesw")

    tile_1_0.grid(row=1, column=0, sticky="nesw")
    tile_1_1.grid(row=1, column=1, sticky="nesw")
    tile_1_2.grid(row=1, column=2, sticky="nesw")
    tile_1_3.grid(row=1, column=3, sticky="nesw")
    tile_1_4.grid(row=1, column=4, sticky="nesw")

    tile_2_0.grid(row=2, column=0, sticky="nesw")
    tile_2_1.grid(row=2, column=1, sticky="nesw")
    tile_2_2.grid(row=2, column=2, sticky="nesw")
    tile_2_3.grid(row=2, column=3, sticky="nesw")
    tile_2_4.grid(row=2, column=4, sticky="nesw")

    tile_3_0.grid(row=3, column=0, sticky="nesw")
    tile_3_1.grid(row=3, column=1, sticky="nesw")
    tile_3_2.grid(row=3, column=2, sticky="nesw")
    tile_3_3.grid(row=3, column=3, sticky="nesw")
    tile_3_4.grid(row=3, column=4, sticky="nesw")

    tile_4_0.grid(row=4, column=0, sticky="nesw")
    tile_4_1.grid(row=4, column=1, sticky="nesw")
    tile_4_2.grid(row=4, column=2, sticky="nesw")
    tile_4_3.grid(row=4, column=3, sticky="nesw")
    tile_4_4.grid(row=4, column=4, sticky="nesw")

def get_tile_type(height_coordinate, width_coordinate):
    color = "black"
    if matrix[height_coordinate][width_coordinate] == 0:
        color = "brown"
    if matrix[height_coordinate][width_coordinate] == 1:
        color = "green"
    if matrix[height_coordinate][width_coordinate] == 2:
        color = "blue"
    if matrix[height_coordinate][width_coordinate] == 3:
        color = "orange"
    if matrix[height_coordinate][width_coordinate] == 4:
        color = "yellow"
    if matrix[height_coordinate][width_coordinate] == 5:
        color = "red"
    return color


# noinspection PyGlobalUndefined
def tile_type_creator():
    global map_height
    global map_width
    map_height = 5
    map_width = 5

    global matrix
    matrix = [[1 for x in range(map_height)] for y in range(map_width)]

    height_coordinates, width_coordinates = rng(map_height, map_width)
    height_coordinates = height_coordinates - 1
    width_coordinates = width_coordinates - 1
    matrix[height_coordinates][width_coordinates] = 2

    amount_tree = int((map_height*map_width)/3)
    for count_tree in range(amount_tree):
        height_coordinates, width_coordinates = rng(map_height, map_width)
        height_coordinates = height_coordinates - 1
        width_coordinates = width_coordinates - 1

        while matrix[height_coordinates][width_coordinates] != 1:
            amount_tree = amount_tree + 1
            height_coordinates, width_coordinates = rng(map_height, map_width)
            height_coordinates = height_coordinates - 1
            width_coordinates = width_coordinates - 1

        matrix[height_coordinates][width_coordinates] = 0

    height_coordinates, width_coordinates = rng(map_height, map_width)
    height_coordinates = height_coordinates - 1
    width_coordinates = width_coordinates - 1
    while matrix[height_coordinates][width_coordinates] != 1:
        amount_tree = amount_tree + 1
        height_coordinates, width_coordinates = rng(map_height, map_width)
        height_coordinates = height_coordinates - 1
        width_coordinates = width_coordinates - 1
    matrix[height_coordinates][width_coordinates] = 3

    while matrix[height_coordinates][width_coordinates] != 1:
        amount_tree = amount_tree + 1
        height_coordinates, width_coordinates = rng(map_height, map_width)
        height_coordinates = height_coordinates - 1
        width_coordinates = width_coordinates - 1
    matrix[height_coordinates][width_coordinates] = 4

    while matrix[height_coordinates][width_coordinates] != 1:
        amount_tree = amount_tree + 1
        height_coordinates, width_coordinates = rng(map_height, map_width)
        height_coordinates = height_coordinates - 1
        width_coordinates = width_coordinates - 1
    matrix[height_coordinates][width_coordinates] = 5

# noinspection PyGlobalUndefined
def check_game_beatable():
    global game_beatable
    matrix_check = copy.deepcopy(matrix)
    for x in range(map_height):
        for y in range(map_width):
            if matrix_check[x][y] == 2:
                matrix_check[x][y] = 1
            if matrix_check[x][y] == 3:
                matrix_check[x][y] = 1
            if matrix_check[x][y] == 4:
                matrix_check[x][y] = 1
            if matrix_check[x][y] == 5:
                matrix_check[x][y] = 0

    grid = Grid(matrix=matrix_check)
    finder = AStarFinder()

    start_height, start_width = search_tile_state(2)
    chest_height, chest_width = search_tile_state(3)
    key_height, key_width = search_tile_state(4)
    boss_height, boss_width = search_tile_state(5)

    start = grid.node(start_width, start_height)
    key = grid.node(key_width, key_height)
    chest = grid.node(chest_width, chest_height)

    path, runs = finder.find_path(start, key, grid)
    if path:
        Grid.cleanup(grid)
        path, runs = finder.find_path(key, chest, grid)
        if path:
            Grid.cleanup(grid)
            matrix_check[boss_height][boss_width] = 1
            grid_boss = Grid(matrix=matrix_check)
            chest = grid_boss.node(chest_width, chest_height)
            boss = grid_boss.node(boss_width, boss_height)
            path, runs = finder.find_path(chest, boss, grid_boss)
            if path:
                game_beatable = 1
            else:
                game_beatable = 0
        else:
            game_beatable = 0
    else:
        game_beatable = 0
    Grid.cleanup(grid)

# noinspection PyGlobalUndefined
def search_tile_state(tile_value):
    tile_height = 0
    tile_width = 0
    for x in range(map_height):
        for y in range(map_width):
            if matrix[x][y] == tile_value:
                tile_height = x
                tile_width = y
    #print(tile_height, "t", tile_value)
    return tile_height, tile_width

def check_tile_state(tile_height_coordinate, tile_width_coordinate):
    tile_state = matrix[tile_height_coordinate][tile_width_coordinate]
    return tile_state

window = tk.Tk()

main()

#window.mainloop()
