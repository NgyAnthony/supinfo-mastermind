def check_array(code_array: list, game_array: list):
    """
    :param code_array: Array of the answer code (randomized or chosen by other player)
    :param game_array: Array of the line of colors set by the player
    :return: Array of pawns for validation either Red(color and position), White(color) or empty(none)
    """
    checker_array = []

    for index in range(len(code_array)):
        color_in_line = game_array[index]
        color_in_code = code_array[index]

        # Same color and same position, set red pawn
        if color_in_code == color_in_line:
            checker_array.append("Rouge")

        # Color is in the answer, but not at the right position, set white pawn
        elif color_in_line in code_array:
            checker_array.append("Blanc")

        # Colors isn't in the answer.
        else:
            checker_array.append("Vide")

    # Array must be of length of 4 (it verified each color of the line)
    if len(checker_array) != 4:
        raise ValueError('Unexpected error, verify checker array length. Checker array: ', checker_array)

    print("---Check_array---")
    print("Game board array is: ", game_array)
    print("Answer code is: ", code_array)
    return checker_array
