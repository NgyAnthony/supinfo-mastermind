import random

ROWS = 10
COLS = 6
COLOR_ARR = ["Green", "Blue", "Orange", "Red", "Yellow", "Purple"]


class Model:
    def __init__(self):
        # Define the number of cols and rows you want (i.e 6 cols = 2 dedicated for the numbers and the hints)
        self.rows = ROWS
        self.cols = COLS

        # MAYBE USELESS
        '''self.colors_dict = (
            {0: "Green"},
            {1: "Blue"},
            {2: "Orange"},
            {3: "Red"},
            {4: "Yellow"},
            {5: "Purple"})'''

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
