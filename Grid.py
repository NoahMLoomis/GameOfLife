import turtle

SCREEN_SIZE = 600

t = turtle.Turtle(visible=False)
wn = turtle.Screen()
wn.setup(SCREEN_SIZE, SCREEN_SIZE)
wn.tracer(0)

class GridClass:
    def __init__(self, num_rows, grid=[]):
        self.num_rows = num_rows
        self.num_cols = num_rows
        self.grid = grid
        
        if self.grid == []:
            for row in range(num_rows):
                for col in range(num_rows):
                    self.grid.append([row, col, 0])


    def draw_square(self, start_x, start_y, size_of_square, is_square_alive):
        t.goto(start_x, start_y)
        if is_square_alive == 1:
                t.fillcolor("green")
                t.begin_fill()
        t.pendown()
        for i in range(4):
            t.forward(size_of_square)
            t.right(90)
        t.end_fill()
        t.penup()
    
    
    def draw_grid(self):
        size_of_square = SCREEN_SIZE /self.num_rows
        t.penup()
        start_x, start_y = -300, -300
                
        for row in range(self.num_rows):
            start_y += size_of_square
            start_x = -300
            for col in range(self.num_rows):
                self.draw_square(start_x, start_y, size_of_square, self.grid[int(f'{row}{col}')][2])
                start_x += size_of_square
        

wn.exitonclick()