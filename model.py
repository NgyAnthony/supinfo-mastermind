import random

ROWS = 6
COLS = 6
COLOR_ARR = ["Green", "Blue", "Orange", "Red", "Yellow", "Purple"]


class Model:
    def __init__(self):
        # Define the number of cols and rows you want (i.e 6 cols = 2 dedicated for the numbers and the hints)
        self.rows = ROWS
        self.cols = COLS
        self.PLAYABLE_ROWS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.PLAYABLE_COLS = [6, 8, 10]

        # MAYBE USELESS
        '''self.colors_dict = (
            {0: "Green"},
            {1: "Blue"},
            {2: "Orange"},
            {3: "Red"},
            {4: "Yellow"},
            {5: "Purple"})'''

        self.colors_arr = COLOR_ARR

        # Array of Tkinter circles (integer pointer) in the game line
        self.circles_line: list = []

        # Hints shown at the last column
        self.current_hints: list = []

        # Index of the current row being played
        self.current_row: int = 0

        # Index of the current color chosen by the player
        self.current_color = None

        self.game_over = False
        self.game_won = None

        self.set_game_context()

    def set_game_context(self):
        # Array of the answer
        self.code: list = [None] * (self.cols - 2)

        # Array of the current line being used in the game_board
        self.game_line: list = [None] * (self.cols - 2)

    def place_color(self, color, pos):
        """
        Set the color inside the current line being used at the correct position.

        :param color: Integer of the color represented
        :param pos: Index of the position in the line
        """
        self.game_line[pos] = color
        print("Placing {} at index {}.".format(color, pos))

    def generate_code(self):
        """
        Generate a random code.
        """
        for idx, value in enumerate(self.code):
            self.code[idx] = random.choice(self.colors_arr)

        print("---Start Generate code---")
        print("Generated random code: ", self.code)
        print("---End Generate code---")

    def reset_model(self):
        # Define the number of cols and rows you want (i.e 6 cols = 2 dedicated for the numbers and the hints)
        self.rows = ROWS
        self.cols = COLS

        self.colors_arr = COLOR_ARR

        # Array of the answer
        self.code: list = [None] * (self.cols - 2)

        # Array of the current line being used in the game_board
        self.game_line: list = [None] * (self.cols - 2)

        # Array of Tkinter circles (integer pointer) in the game line
        self.circles_line: list = []

        # Hints shown at the last column
        self.current_hints: list = []

        # Index of the current row being played
        self.current_row: int = 0

        # Index of the current color chosen by the player
        self.current_color = None

        self.game_over = False
        self.game_won = None

    def set_code(self, new_code):
        exception_flag = False
        for color in new_code:
            if color.get() not in self.colors_arr:
                exception_flag = True

        for x in range(len(new_code)):
            if exception_flag is False:
                self.code[x] = new_code[x].get()

        if exception_flag:
            print("Code entered was invalid, ignoring request", new_code)
        else:
            print("---Start code set---")
            print("New code has been set: ", self.code)
