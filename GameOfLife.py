from Grid import GridClass
import random, copy


class GameOfLife:
    def __init__(self, game_grid=[], universe_size=4):
        self.game_grid = game_grid
        self.universe_size = universe_size

    def create_grid(self):
        self.game_grid = GridClass(square_size=self.universe_size)

    def populate_randomized(self):
        for cell in self.game_grid.grid:
            if random.random() < 0.4:
                self.game_grid.change_alive_status(cell)

    def play_sequence(self):
        grid_copy = copy.deepcopy(self.game_grid)
        for index in range(len(grid_copy.grid)):
            if grid_copy.get_cell_alive_status(grid_copy.grid[index]) == 1:
                self.check_overpopulation(index, grid_copy)

    def check_overpopulation(self, index, grid_copy):
        alive_count = 0
        left = grid_copy.grid[index - 1]
        right = grid_copy.grid[index + 1]
        top = grid_copy.get_cell(grid_copy.grid[0], grid_copy.grid[1] + 1)
        # bottom = grid_copy.grid[]
        # left_bot_diag = grid_copy.grid[]
        # right_bot_diag = grid_copy.grid[]
        # left_top_diag = grid_copy.grid[]
        # right_top_diag = grid_copy.grid[]
        
        while not IndexError:
            if left[2] == 1:
                alive_count += 1
            if right[2] == 1:
                alive_count += 1
            if alive_count > 3:
                grid_copy.change_alive_status(grid_copy.grid[index])
            
        
        
    # def check_statis(self):
    
    # def check_underpopulation(self):
        
    
    # def check_reproduction(self):
    
    
g = GameOfLife()
g.create_grid()
g.populate_randomized()
g.play_sequence()
