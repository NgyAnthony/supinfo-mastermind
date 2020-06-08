import random
from check_array import check

# Array of the answer
code = ['x', 'x', 'x', 'x']

# Array of the current line being used in the game_board
game_line = ['x', 'x', 'x', 'x']


def get_line():
    return game_line


def place_color(arr, color, pos):
    """
    Set the color inside the line of the game at the correct position.

    :param arr: Array of the line being used
    :param color: Integer of the color represented
    :param pos: Index of the position in the line
    """
    arr[pos] = color
    print("Placing {} at index {}.".format(color, pos))


def generate_code(arr):
    """
    :param arr: Placeholder array for the generation of the code
    """
    for idx, value in enumerate(arr):
        arr[idx] = random.randint(0, 5)

    print("---Start Generate code---")
    print("Generated random code: ", arr)
    print("---End Generate code---")


# Testing
generate_code(code)
place_color(game_line, 1, 0)
place_color(game_line, 5, 1)
place_color(game_line, 3, 2)
place_color(game_line, 4, 3)
check(code, game_line)
