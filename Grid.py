# import turtle

# SCREEN_SIZE = 600

# t = turtle.Turtle(visible=False)
# wn = turtle.Screen()
# wn.setup(SCREEN_SIZE, SCREEN_SIZE)
# wn.tracer(0)

class GridClass:
    def __init__(self, square_size, grid=[]):
        self.square_size = square_size
        self.grid = grid
        
        if self.grid == []:
            for row in range(square_size):
                for col in range(square_size):
                    self.grid.append([row, col, 0])
                    
    def change_alive_status(self, cell):
        # cell = self.get_cell(x_pos, y_pos)
        if  self.get_cell_alive_status(cell) == 0:
            cell[2] = 1
        elif self.get_cell_alive_status(cell) == 1:
            cell[2] = 0
            
    def get_cell(self, x_pos, y_pos):
        for cell in self.grid:
            if cell[0] == x_pos and cell[1] == y_pos:
                return cell
        return None
    
        

    def get_cell_alive_status(self, cell):
        return cell[2]
    
    # def draw_square(self, start_x, start_y, size_of_square, is_square_alive):
    #     t.goto(start_x, start_y)
    #     if is_square_alive == 1:
    #             t.fillcolor("green")
    #             t.begin_fill()
    #     t.pendown()
    #     for i in range(4):
    #         t.forward(size_of_square)
    #         t.right(90)
    #     t.end_fill()
    #     t.penup()
    
    
    # def draw_grid(self):
    #     size_of_square = SCREEN_SIZE /self.num_rows
    #     t.penup()
    #     start_x, start_y = -300, -300
                
    #     for row in range(self.num_rows):
    #         start_y += size_of_square
    #         start_x = -300
    #         for col in range(self.num_rows):
    #             self.draw_square(start_x, start_y, size_of_square, self.grid[int(f'{row}{col}')][2])
    #             start_x += size_of_square
        

# wn.exitonclick()