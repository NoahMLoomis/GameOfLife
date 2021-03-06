import tkinter
import turtle
from tkinter import *
from tkinter import messagebox
import time

from GameOfLife import GameOfLife
from Grid import Grid
from FileReading import FileReading


class InvalidInputException(BaseException):
    pass


class PausedException(BaseException):
    pass


class GUI:
    def __init__(self, t, wn, screen_size=600, grid_size=10, grid=None):
        self.grid_size = grid_size
        self.grid_area_positions = []
        self.screen_size = screen_size

        if grid == None:
            self.game_of_life = GameOfLife(game_grid=Grid(rows=grid_size))
        else:
            self.game_of_life = GameOfLife(
                game_grid=Grid(grid=grid, rows=grid_size))

        self.size_of_square = self.screen_size / self.game_of_life.game_grid.rows

        self.t = t
        self.wn = wn
        self.wn.setup(self.screen_size + 100, self.screen_size + 100)
        self.wn.tracer(0)

        

        self.wn.onkey(self.quit, 'q')
        self.wn.onkey(self.loop, 's')
        self.wn.onkey(self.r_press, 'r')
        self.wn.onkey(self.p_press, 'p')


        self.wn.listen()
        self.wn.onclick(self.click_cell)

        self.draw_grid()

    def r_press(self):
        self.game_of_life.populate_randomized()
        self.draw_grid()
    
    def p_press(self):
        raise PausedException()

    def loop(self):
        while True:
            time.sleep(0.5)
            try:
                self.wn.ontimer(fun=self.s_press, t=1)
            except PausedException:
                print("Paused")

    def s_press(self):
        self.game_of_life.play_sequence()
        self.draw_grid()

    def draw_square(self, start_x, start_y, size_of_square, is_square_alive):
        self.t.goto(start_x, start_y)
        if is_square_alive == 1:
            self.t.fillcolor("green")
            self.t.begin_fill()
        else:
            self.t.fillcolor("white")
            self.t.begin_fill()
        self.t.pendown()
        for _ in range(4):
            self.t.forward(size_of_square)
            self.t.left(90)
        self.t.end_fill()
        self.t.penup()

    def get_cell_from_grid(self, x_pos, y_pos):
        for area_coords in self.grid_area_positions:
            if x_pos >= area_coords[0] and x_pos < area_coords[1] and y_pos >= area_coords[2] and y_pos < area_coords[3]:
                return area_coords[4]

    def click_cell(self, x_pos, y_pos):
        cell_to_change = self.get_cell_from_grid(x_pos, y_pos)
        self.game_of_life.game_grid.change_alive_status(cell_to_change)
        self.draw_grid()

    def draw_grid(self):

        self.t.penup()
        start_x, start_y = -300, -300

        for row in range(self.game_of_life.game_grid.rows):
            start_x = -300
            for col in range(self.game_of_life.game_grid.rows):
                self.draw_square(start_x, start_y, self.size_of_square,
                                 self.game_of_life.game_grid.get_cell(row, col)[2])

                # This appends the areas that each square occupies,
                # and the cell associated with it, needed for the click_cell
                self.grid_area_positions.append((
                    start_x,
                    start_x + self.size_of_square,
                    start_y,
                    start_y + self.size_of_square,
                    self.game_of_life.game_grid.get_cell(row, col))
                )
                start_x += self.size_of_square
            start_y += self.size_of_square

    def quit(self):
        self.wn.bye()


if __name__ == "__main__":
    t = turtle.Turtle(visible=False)
    wn = turtle.Screen()
    
    root = Tk()
    root.geometry("400x400")
    
    frame = Frame(root, width=500, height=400, bd=1)
    frame.pack()
    
    lbl_r = Label(frame, text="R: Randomly populate the grid\nS: Start the Game\nP: Pause the Game\nQ: Quit the game")
    
    lbl_r.pack(side='left')
    
    while True:
        try:
            num_rows = wn.textinput(
                "Enter a name of a file, or number", "Enter a value")
            num_rows = int(num_rows)
            if num_rows < 3 or num_rows > 20:
                raise InvalidInputException(
                    "Number cannot be less than 3 or greater than 20")

            g = GUI(grid_size=num_rows, t=t, wn=wn)

        except ValueError:
            try:
                f = FileReading(num_rows)
                g = GUI(grid=f.transform_to_grid(),
                        grid_size=f.rows, t=t, wn=wn)
            except FileNotFoundError as msg:
                messagebox.showerror("Invalid Input", msg)
        except InvalidInputException as msg:
            messagebox.showerror("Invalid Input", msg)
        except (TclError, TypeError):
            break

        tkinter.mainloop()
