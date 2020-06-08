import random
from check_array import check_array

code_array = ['x', 'x', 'x', 'x']
game_board_array = ['x', 'x', 'x', 'x']


def place(arr, color, pos):
    # replace array postion by color
    arr[pos] = color
    print("Placing {} at index {}.".format(color, pos))
    return arr


def generate_code(arr):
    # iterate on arr to replace x by random num
    for idx, value in enumerate(arr):
        arr[idx] = random.randint(0, 5)

    print("Generated random code: ", arr)
    return arr


generate_code(code_array)
place(game_board_array, 1, 0)
place(game_board_array, 5, 1)
place(game_board_array, 3, 2)
place(game_board_array, 4, 3)
print(check_array(code_array, game_board_array))
