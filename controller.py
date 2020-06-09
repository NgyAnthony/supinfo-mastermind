from model import Model


class Controller:
    def __init__(self):
        self.model = Model()
        self.model.generate_code()

    def check(self):
        """
        Compare the current line being used to the answer code.

        :return: Array of pawns for validation either Red(color and position), White(color) or empty(none)
        """
        hints = []

        for index in range(len(self.model.code)):
            color_in_line = self.model.game_line[index]
            color_in_code = self.model.code[index]

            # Same color and same position, set red pawn
            if color_in_code == color_in_line:
                hints.append("Red")

            # Color is in the answer, but not at the right position, set white pawn
            elif color_in_line in self.model.code:
                hints.append("White")

            # Colors isn't in the answer.
            else:
                hints.append("Black")

        # Array must be of length of 4 (it verified each color of the line)
        if len(hints) != (self.model.cols - 2):
            raise ValueError('Unexpected error, verify hints array length. hints array: ', hints)

        print("---Start array check---")
        print("Game board array is: ", self.model.game_line)
        print("Answer code is: ", self.model.code)
        print("Hint pawns are: ", hints)

        return hints

    def handle_color_click(self, tags):
        # Get the color selected and inject it into the model
        color = tags[0]
        self.model.current_color = color
        print('Color "{}" registered.'.format(color))

    def handle_click(self, tags):
        row = int(tags[0])
        col = int(tags[1])
        if self.model.current_color in self.model.colors_arr and self.model.current_row == row:
            self.model.game_line[col - 1] = self.model.current_color
        else:
            print("Can't handle")

    def handle_delete_line(self):
        self.model.game_line = [None] * self.model.cols
        self.model.circles_line = []

    def handle_check(self):
        # Find out if you can call the check function
        if None not in self.model.game_line and len(self.model.current_hints) == 0:
            self.model.current_hints = self.check()
            self.model.current_row += 1
        elif None in self.model.game_line:
            pass
        else:
            raise ValueError("Unexpected error: line checked before it is filled.")

    def game_over(self):
        only_red = len(set(self.model.current_hints)) == 1 and self.model.current_hints[0] == "Red"
        if only_red:
            self.model.game_over = True
            self.model.won = True

        elif self.model.current_row == self.model.rows:
            self.model.game_over = True
            self.model.won = False
        else:
            self.model.game_over = False
