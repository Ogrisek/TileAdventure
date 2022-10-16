import random
import tkinter as tk

def main():
    start_fenster()
    #game_fenster_update()
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

def start_button_creator():
    # noinspection PyGlobalUndefined
    global start_button
    start_button = tk.Button(text="Click me!", background="turquoise")
    start_button.bind("<Button-1>", handle_click_start)
    start_button.pack()
    # noinspection PyGlobalUndefined
    global game_beatable
    game_beatable = 0

def handle_click_start(event):
    start_button.destroy()
    quit_button.destroy()
    # noinspection PyGlobalUndefined
    global game_beatable
    #game_beatable = 0
    # noinspection PyGlobalUndefined
    #global game_beatable
    while game_beatable == 0:
        tile_type_creator()
        check_game_beatable()
    game_frame_creator()

def game_fenster():
    greeting = tk.Label(text="Daniel ist ein netter Mensch")
    greeting.pack()

def game_frame_creator():
    window.geometry("512x512")
    screen_height_setting = 5
    screen_width_setting = 5

    for screen_height in range(screen_height_setting):
        window.rowconfigure(screen_height, minsize=64)
        for screen_width in range(screen_width_setting):
            window.columnconfigure(screen_width, minsize=64)
            # noinspection PyGlobalUndefined
            global frame_game
            frame_game = tk.Frame(master=window)
            frame_game.grid(row=screen_height, column=screen_width)
            tile_label = tk.Label(master=frame_game, text=f"Row {screen_height}\nColumn {screen_width}")
            tile_label.grid()
            tile_updater()

def tile_updater():
    #get color for tile typ

    tile_type_0_0 = "green"
    tile_type_0_1 = "blue"
    tile_type_0_2 = get_tile_type()
    tile_type_0_3 = "blue"
    tile_type_0_4 = "blue"

    tile_type_1_0 = "blue"
    tile_type_1_1 = "blue"
    tile_type_1_2 = "blue"
    tile_type_1_3 = "blue"
    tile_type_1_4 = "blue"

    tile_type_2_0 = "blue"
    tile_type_2_1 = "blue"
    tile_type_2_2 = "blue"
    tile_type_2_3 = "blue"
    tile_type_2_4 = "blue"

    tile_type_3_0 = "blue"
    tile_type_3_1 = "blue"
    tile_type_3_2 = "blue"
    tile_type_3_3 = "blue"
    tile_type_3_4 = "blue"

    tile_type_4_0 = "blue"
    tile_type_4_1 = "blue"
    tile_type_4_2 = "blue"
    tile_type_4_3 = "blue"
    tile_type_4_4 = "blue"

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

def get_tile_type():
    color = "green"
    return color

def tile_type_creator():
    # noinspection PyGlobalUndefined
    global map_height
    # noinspection PyGlobalUndefined
    global map_width
    map_height = 5
    map_width = 5

    # noinspection PyGlobalUndefined
    global matrix
    matrix = [[0 for x in range(map_height)] for y in range(map_width)]

    height_coordinates, width_coordinates = rng(map_height, map_width)
    height_coordinates = height_coordinates - 1
    width_coordinates = width_coordinates - 1
    matrix[height_coordinates][width_coordinates] = 2

    #count_tree = 0
    amount_tree = int((map_height*map_width)/3)
    #print(amount_tree)
    for count_tree in range(amount_tree):
        height_coordinates, width_coordinates = rng(map_height, map_width)
        height_coordinates = height_coordinates - 1
        width_coordinates = width_coordinates - 1
        #print(height_coordinates)
        #print(width_coordinates)

        while matrix[height_coordinates][width_coordinates] != 0:
            amount_tree = amount_tree + 1
            height_coordinates, width_coordinates = rng(map_height, map_width)
            height_coordinates = height_coordinates - 1
            width_coordinates = width_coordinates - 1

        matrix[height_coordinates][width_coordinates] = 1

    height_coordinates, width_coordinates = rng(map_height, map_width)
    height_coordinates = height_coordinates - 1
    width_coordinates = width_coordinates - 1
    while matrix[height_coordinates][width_coordinates] != 0:
        amount_tree = amount_tree + 1
        height_coordinates, width_coordinates = rng(map_height, map_width)
        height_coordinates = height_coordinates - 1
        width_coordinates = width_coordinates - 1
    matrix[height_coordinates][width_coordinates] = 3

    while matrix[height_coordinates][width_coordinates] != 0:
        amount_tree = amount_tree + 1
        height_coordinates, width_coordinates = rng(map_height, map_width)
        height_coordinates = height_coordinates - 1
        width_coordinates = width_coordinates - 1
    matrix[height_coordinates][width_coordinates] = 4

    while matrix[height_coordinates][width_coordinates] != 0:
        amount_tree = amount_tree + 1
        height_coordinates, width_coordinates = rng(map_height, map_width)
        height_coordinates = height_coordinates - 1
        width_coordinates = width_coordinates - 1
    matrix[height_coordinates][width_coordinates] = 5

    for x in range(5):
        print(matrix[x][0], matrix[x][1], matrix[x][2], matrix[x][3], matrix[x][4])
    #matrix[0][0] = 3
    #print(matrix[0][0])
    #print(matrix[0][1])

def check_game_beatable():
    #trial and error path finder
    print(matrix[0][0])
    # noinspection PyGlobalUndefined
    global game_beatable
    game_beatable = 1
    # noinspection PyGlobalUndefined
    global player_height
    # noinspection PyGlobalUndefined
    global player_width

    for x in range(map_height):
        for y in range(map_width):
            if matrix[x][y] == 2:
                player_height = x
                player_width = y

    print(player_height, player_width)

    #for player_height in range(map_height):
    #    for player_width in range(map_width):


window = tk.Tk()

main()

#window.mainloop()
