def check(code: list, game_line: list):
    """
    :param code: Array of the answer code (randomized or chosen by other player)
    :param game_line: Array of the line of colors set by the player
    :return: Array of pawns for validation either Red(color and position), White(color) or empty(none)
    """
    hints = []

    for index in range(len(code)):
        color_in_line = game_line[index]
        color_in_code = code[index]

        # Same color and same position, set red pawn
        if color_in_code == color_in_line:
            hints.append("Rouge")

        # Color is in the answer, but not at the right position, set white pawn
        elif color_in_line in code:
            hints.append("Blanc")

        # Colors isn't in the answer.
        else:
            hints.append("Vide")

    # Array must be of length of 4 (it verified each color of the line)
    if len(hints) != 4:
        raise ValueError('Unexpected error, verify hints array length. hints array: ', hints)

    print("---Start array check---")
    print("Game board array is: ", game_line)
    print("Answer code is: ", code)
    print("Hint pawns are: ", hints)
    print("---End array check---")

    return hints
