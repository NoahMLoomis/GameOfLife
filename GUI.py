import turtle, tkinter

from GameOfLife import GameOfLife
from Grid import Grid


class GUI:
    def __init__(self, screen_size=600, grid_size = 10):
        self.screen_size = screen_size
        self.t = turtle.Turtle(visible=False)
        self.wn = turtle.Screen()

        self.wn.setup(self.screen_size + 100, self.screen_size + 100)
        self.wn.tracer(0)

        # self.wn.onclick(self.click_cell)
        self.wn.onkey(self.quit, 'q')

        # self.wn.ontimer()
        
        self.wn.listen()
        self.wn.onclick(self.click_cell)

        
        self.game_grid = Grid(grid_size)
        self.game_of_life = GameOfLife(universe_size=6, game_grid=self.game_grid)
        self.size_of_square = self.screen_size / self.game_grid.rows


    def draw_square(self, start_x, start_y, size_of_square, is_square_alive):
        self.t.goto(start_x, start_y)
        if is_square_alive == 1:
            self.t.fillcolor("green")
            self.t.begin_fill()
        self.t.pendown()
        for _ in range(4):
            self.t.forward(size_of_square)
            self.t.right(90)
        self.t.end_fill()
        self.t.penup()

    def click_cell(self, x_pos, y_pos):
        grid_x_pos = x_pos * 300

        cell_to_change = self.game_grid.get_cell(0, 0)
        self.game_grid.change_alive_status(cell_to_change)
        self.draw_grid()

    def draw_grid(self):
        
        self.t.penup()
        start_x, start_y = -300, -300

        for row in range(self.game_grid.rows):
            start_y += self.size_of_square
            start_x = -300
            for col in range(self.game_grid.rows):
                self.draw_square(start_x, start_y, self.size_of_square,
                                 self.game_grid.get_cell(row, col)[2])
                start_x += self.size_of_square
    
    def quit(self):
        self.wn.bye()


g = GUI(grid_size=20)
g.game_of_life.populate_randomized()
g.draw_grid()
tkinter.mainloop()