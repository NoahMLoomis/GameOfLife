import turtle

from GameOfLife import GameOfLife
from Grid import Grid


class GUI:
    def __init__(self, screen_size=600):
        self.screen_size = screen_size

        self.t = turtle.Turtle(visible=False)
        self.wn = turtle.Screen()

        self.wn.setup(self.screen_size + 100, self.screen_size + 100)
        self.wn.tracer(0)
        
        self.game_grid = Grid(10)
        self.game_of_life = GameOfLife(universe_size=6, game_grid=self.game_grid)

    def draw_square(self, start_x, start_y, size_of_square, is_square_alive):
        self.t.goto(start_x, start_y)
        if is_square_alive == 1:
            self.t.fillcolor("green")
            self.t.begin_fill()
        self.t.pendown()
        for i in range(4):
            self.t.forward(size_of_square)
            self.t.right(90)
        self.t.end_fill()
        self.t.penup()

    def draw_grid(self):
        size_of_square = self.screen_size / self.game_grid.rows
        self.t.penup()
        start_x, start_y = -300, -300

        for row in range(self.game_grid.rows):
            start_y += size_of_square
            start_x = -300
            for col in range(self.game_grid.rows):
                self.draw_square(start_x, start_y, size_of_square,
                                 self.game_grid.grid[int(f'{row}{col}')][2])
                start_x += size_of_square


g = GUI()
g.game_of_life.populate_randomized()
g.draw_grid()
g.wn.exitonclick()
