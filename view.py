from tkinter import *
from controller import Controller

# Specific configuration for the width and height of each element
WINDOW_WIDTH = 1366
WINDOW_HEIGHT = 768

HEIGHT_PADDING = WINDOW_HEIGHT * 0.05
WIDTH_PADDING = WINDOW_WIDTH * 0.05

CONTAINER_UI_HEIGHT = WINDOW_HEIGHT * 0.90
CONTAINER_UI_WIDTH = WINDOW_WIDTH * 0.3

CONTAINER_GAME_HEIGHT = WINDOW_HEIGHT * 0.90
CONTAINER_GAME_WIDTH = WINDOW_WIDTH * 0.7

GAME_FRAME_HEIGHT = CONTAINER_GAME_HEIGHT * 0.90
GAME_FRAME_WIDTH = CONTAINER_GAME_WIDTH

COLOR_FRAME_HEIGHT = CONTAINER_GAME_HEIGHT * 0.10
COLOR_FRAME_WIDTH = CONTAINER_GAME_WIDTH


class View:
    def __init__(self):
        # Tkinter master window
        self.parent = Tk()

        # Initiate controller and model
        self.controller = Controller()
        self.model = self.controller.model

        # Initiate a frame that will contain the UI
        self.ui_frame = Frame(master=self.parent, height=CONTAINER_UI_HEIGHT, width=CONTAINER_UI_WIDTH, bd=1, relief=SUNKEN)

        # Initiate a container that will contain the game and the color palette above the game board
        self.game_container = Frame(master=self.parent, height=CONTAINER_GAME_HEIGHT, width=CONTAINER_GAME_WIDTH, bd=1, relief=SUNKEN)
        self.game_frame = Frame(master=self.game_container, height=GAME_FRAME_HEIGHT, width=GAME_FRAME_WIDTH)
        self.color_frame = Frame(master=self.game_container, height=COLOR_FRAME_HEIGHT, width=COLOR_FRAME_WIDTH, bd=1, relief=SUNKEN)

        # Placeholder for the circle geometry attached to the cursor
        self.attached_circle = "Null"

        # Attach a canvas to the game board and another to the color palette frame
        self.canvas = Canvas(self.game_frame, height=GAME_FRAME_HEIGHT, width=GAME_FRAME_WIDTH)
        self.color_canvas = Canvas(self.color_frame, height=COLOR_FRAME_HEIGHT, width=COLOR_FRAME_WIDTH)

        # Set the number of rows and cols you want
        self.rows = self.model.rows
        self.cols = self.model.cols
        (self.sq_sz_x, self.sq_sz_y) = (GAME_FRAME_WIDTH // self.cols, GAME_FRAME_HEIGHT // self.rows)

        # Make the UI appear
        self.draw_board()

        mainloop()

    def draw_board(self):
        # Draw the whole board (frame, canvas)
        self.canvas.pack()
        self.color_canvas.pack()
        self.color_frame.pack()
        self.game_frame.pack()

        self.game_container.pack(side=LEFT, padx=WIDTH_PADDING, pady=HEIGHT_PADDING)
        self.ui_frame.pack(side=RIGHT, padx=WIDTH_PADDING, pady=HEIGHT_PADDING)

        self.draw_grid()
        self.draw_ui()
        self.draw_palette()

    def draw_grid(self):
        # Draws the grid for the game canvas
        for row in range(self.rows):
            for col in range(self.cols):
                x0 = (col * self.sq_sz_x)
                y0 = (row * self.sq_sz_y)
                x1 = x0 + self.sq_sz_x
                y1 = y0 + self.sq_sz_y

                x_center = x0 + self.sq_sz_x/2
                y_center = y0 + self.sq_sz_y/2

                rectangle_instance = self.canvas.create_rectangle(x0, y0, x1, y1, outline="black",
                                                                  fill="lightgrey", tags=(row, col, x_center, y_center))
                self.canvas.tag_bind(rectangle_instance, '<ButtonPress-1>', self.on_object_click)

                if col == 0:
                    # Draws the numbers on the first column
                    self.draw_number(x_center, y_center, row)
                if (col != self.cols - 1) and col != 0:
                    # Draws the small circles on the playable cases
                    self.draw_circle(x_center, y_center, 2.5)

    def draw_ui(self):
        Button(self.ui_frame, text="Delete line", command=self.delete_line).pack()
        Button(self.ui_frame, text="Check line", command=self.check_line).pack()

    def draw_number(self, x_center, y_center, index):
        # Numbers that are on the first column
        self.canvas.create_text(x_center, y_center, text=index)

    def draw_circle(self, x_center, y_center, radius):
        # Helper function used to draw the circles in the palette, those following the cursor, and the ones on the line.
        x0, y0, x1, y1 = self.circle_coords_converter(x_center, y_center, radius)
        self.canvas.create_oval(x0, y0, x1, y1, fill="Black")

    def draw_palette(self):
        # Draw the palette above the game_board
        for index in range(len(self.model.colors_arr)):
            color = self.model.colors_arr[index]

            x_center = (index * COLOR_FRAME_WIDTH/len(self.model.colors_arr)) + self.sq_sz_x/2
            y_center = self.sq_sz_y/2

            x0, y0, x1, y1 = self.circle_coords_converter(x_center, y_center, 15)
            oval_instance = self.color_canvas.create_oval(x0, y0, x1, y1, fill=color, tags=color)
            self.color_canvas.tag_bind(oval_instance, '<ButtonPress-1>', self.on_color_click)

    def circle_coords_converter(self, x_center, y_center, radius):
        # Convert the coordinates of the center of a rectangle to the coordinates of a circle
        return x_center - radius, y_center - radius, x_center + radius, y_center + radius

    def circle_cursor(self, color):
        # Make the circle follow the cursor
        if self.attached_circle != "Null":
            self.canvas.delete(self.attached_circle)
        self.attached_circle = self.canvas.create_oval(0, 0, 0, 0, fill=color)
        self.canvas.bind('<Motion>', self.circle_callback)

    def circle_callback(self, event):
        x, y = event.x, event.y
        # Make sure the circle has a margin from the cursor otherwise the cursor won't be able to trigger events.
        self.canvas.coords(self.attached_circle, x + 15, y, x + 45, y + 30)

    def on_object_click(self, event):
        # Handle click events
        print("--- Rectangle clicked ! ---")
        print('Got object click', event.x, event.y)

        # Finding the rectangle we need and its info
        item = event.widget.find_closest(event.x, event.y)
        tags = self.canvas.gettags(item)

        # Handle the click
        self.controller.handle_click(tags)

        # Check if the game_line has been updated at the specific column
        col = int(tags[1])

        # Create a circle if the game line changed
        if self.model.game_line[col - 1] is not None:
            # Delete the circle attached to the cursor
            self.canvas.delete(self.attached_circle)

            # Find the center of the rectangle clicked
            x_center = float(tags[2])
            y_center = float(tags[3])

            # Get the coordinates and create the circle
            x0, y0, x1, y1 = self.circle_coords_converter(x_center, y_center, 15)
            placed_oval = self.canvas.create_oval(x0, y0, x1, y1, fill=self.model.current_color)

            # Set the created circle in an array to be able to delete it if needed
            self.model.circles_line.append(placed_oval)

            # Set the current color back to none
            self.model.current_color = None

        print("Item number: ", item)
        print("Tags: ", tags)

    def on_color_click(self, event):
        # Handle click events
        print("--- Color clicked ! ---")
        print('Got object click', event.x, event.y)

        # Finding the color we need and its info
        item = event.widget.find_closest(event.x, event.y)
        tags = self.color_canvas.gettags(item)

        # Handle the color click
        self.controller.handle_color_click(tags)

        # Create a circle and associate as long as the current_color isn't null
        if self.model.current_color is not None:
            self.circle_cursor(tags[0])

        print("Item number: ", item)
        print("Tags: ", tags)

    def delete_line(self):
        # Callback of the delete button
        for circle in self.model.circles_line:
            self.canvas.delete(circle)

        self.controller.handle_delete_line()
        print("---Line deleted ! ---")
        print("Check color: ", self.model.current_color)
        print("Check line: ", self.model.game_line)
        print("Check line: ", self.model.circles_line)

    def check_line(self):
        # Callback called when the line is being checked
        self.controller.handle_check()
        if len(self.model.current_hints) == (self.model.cols - 2):
            # Get coords info to place the hint circles in the last col
            last_col = self.model.cols - 1
            current_row = self.model.current_row
            top_left_x = self.sq_sz_x * last_col
            top_left_y = (self.sq_sz_y * current_row) - self.sq_sz_y

            # Color index is used to keep track of the index in current_hints
            color_index = 0

            # 6 board cols -2 = 4 game cols = 2 row and 2 col in the hints so we divide by 2
            for row in range(int(round((self.cols - 2) / 2))):
                for col in range(int(round((self.cols - 2) / 2))):
                    if color_index < self.cols - 2:
                        color_index += 1

                    self.canvas.create_oval(top_left_x + 10 + (10 * col),
                                            top_left_y + 10 + (10 * row),
                                            top_left_x + 10 + (10 * col) + 5,
                                            top_left_y + 10 + (10 * row) + 5, fill=self.model.current_hints[color_index - 1])

            # Reset the current_hints
            self.model.current_hints = []

            # Reset game_line just in case
            self.model.game_line = [None] * (self.cols - 2)

        if self.model.game_over and self.model.game_won:
            # Ask if player wants to play again
            # Show you won
            pass
        elif self.model.game_over and self.model.game_won is False:
            # Ask if player wants to play again
            # Show you lost
            pass
