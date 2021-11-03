from Grid import Grid
import random
import copy


class GameOfLife:
    def __init__(self, game_grid=[]):
        self.game_grid = game_grid

    def populate_randomized(self):
        for cell in self.game_grid.grid:
            if random.random() < 0.4:
                self.game_grid.change_alive_status(cell)

    def play_sequence(self):
        grid_copy = copy.deepcopy(self.game_grid)
        for index in range(len(grid_copy.grid)):
            self.check_death_conditions(index, grid_copy)
        self.game_grid = grid_copy

    def get_cells_to_check(self, x_pos, y_pos, grid_copy):
        if x_pos == 0:
            # Bottom left corner
            if y_pos == 0:
                return [self.get_right_cell(x_pos, y_pos, grid_copy), self.get_top_cell(x_pos, y_pos, grid_copy), self.get_right_top_cell(x_pos, y_pos, grid_copy)]
            # Top left corner
            elif y_pos == self.game_grid.rows - 1:
                return [self.get_bot_cell(x_pos, y_pos, grid_copy), self.get_right_cell(x_pos, y_pos, grid_copy), self.get_right_bot_cell(x_pos, y_pos, grid_copy)]
            # Anywhere else on the x = 0 axis
            else:
                return [self.get_top_cell(x_pos, y_pos, grid_copy),
                        self.get_right_top_cell(x_pos, y_pos, grid_copy),
                        self.get_right_cell(x_pos, y_pos, grid_copy),
                        self.get_right_bot_cell(x_pos, y_pos, grid_copy),
                        self.get_bot_cell(x_pos, y_pos, grid_copy)]
        elif x_pos == self.game_grid.rows - 1:
            # Bottom right corner
            if y_pos == 0:
                return [self.get_left_cell(x_pos, y_pos, grid_copy), self.get_top_cell(x_pos, y_pos, grid_copy), self.get_left_top_cell(x_pos, y_pos, grid_copy)]
            # Top right corner
            elif y_pos == self.game_grid.rows - 1:
                return [self.get_left_cell(x_pos, y_pos, grid_copy), self.get_bot_cell(x_pos, y_pos, grid_copy), self.get_left_bot_cell(x_pos, y_pos, grid_copy)]
            # Anywhere else on the x = self.game_grid.rows - 1 axis
            else:
                return [self.get_left_cell(x_pos, y_pos, grid_copy),
                        self.get_bot_cell(x_pos, y_pos, grid_copy),
                        self.get_left_bot_cell(x_pos, y_pos, grid_copy),
                        self.get_right_top_cell(x_pos, y_pos, grid_copy),
                        self.get_top_cell(x_pos, y_pos, grid_copy)]
        # Checking the bottom y axis
        elif y_pos == 0:
            return [self.get_left_cell(x_pos, y_pos, grid_copy),
                    self.get_left_top_cell(x_pos, y_pos, grid_copy),
                    self.get_top_cell(x_pos, y_pos, grid_copy),
                    self.get_right_top_cell(x_pos, y_pos, grid_copy),
                    self.get_right_cell(x_pos, y_pos, grid_copy)]
        # Checking the top y axis
        elif y_pos == self.game_grid.rows - 1:
            return [self.get_left_cell(x_pos, y_pos, grid_copy),
                    self.get_left_bot_cell(x_pos, y_pos, grid_copy),
                    self.get_bot_cell(x_pos, y_pos, grid_copy),
                    self.get_right_bot_cell(x_pos, y_pos, grid_copy),
                    self.get_right_cell(x_pos, y_pos, grid_copy)]
        # Anywhere that isn't a corner, or on the ends or beginning of the axis
        else:
            return [self.get_left_cell(x_pos, y_pos, grid_copy),
                    self.get_right_cell(x_pos, y_pos, grid_copy),
                    self.get_top_cell(x_pos, y_pos, grid_copy),
                    self.get_bot_cell(x_pos, y_pos, grid_copy),
                    self.get_left_bot_cell(x_pos, y_pos, grid_copy),
                    self.get_right_bot_cell(x_pos, y_pos, grid_copy),
                    self.get_left_top_cell(x_pos, y_pos, grid_copy),
                    self.get_right_top_cell(x_pos, y_pos, grid_copy)]

    def check_death_conditions(self, index, grid_copy):
        x_pos = grid_copy.grid[index][0]
        y_pos = grid_copy.grid[index][1]

        all_checks = self.get_cells_to_check(x_pos, y_pos, grid_copy)

        alive_count = 0

        for cell in all_checks:
            if cell is not None and cell[2] == 1:
                alive_count += 1
                
        if grid_copy.grid[index][2] == 1:
            if alive_count > 3 or alive_count < 2:
                grid_copy.kill_cell(grid_copy.grid[index])
        else:
            if alive_count == 3:
                grid_copy.revive_cell(grid_copy.grid[index])
                            
    def get_right_cell(self, x_pos, y_pos, grid_copy):
        return grid_copy.get_cell(x_pos + 1, y_pos)

    def get_left_cell(self, x_pos, y_pos, grid_copy):
        return grid_copy.get_cell(x_pos - 1, y_pos)

    def get_top_cell(self, x_pos, y_pos, grid_copy):
        return grid_copy.get_cell(x_pos, y_pos + 1)

    def get_bot_cell(self, x_pos, y_pos, grid_copy):
        return grid_copy.get_cell(x_pos, y_pos - 1)

    def get_left_bot_cell(self, x_pos, y_pos, grid_copy):
        return grid_copy.get_cell(x_pos - 1, y_pos - 1)

    def get_right_bot_cell(self, x_pos, y_pos, grid_copy):
        return grid_copy.get_cell(x_pos + 1, y_pos - 1)

    def get_left_top_cell(self, x_pos, y_pos, grid_copy):
        return grid_copy.get_cell(x_pos - 1, y_pos + 1)

    def get_right_top_cell(self, x_pos, y_pos, grid_copy):
        return grid_copy.get_cell(x_pos + 1, y_pos + 1)
# g = GameOfLife()
# g.create_grid()
# g.populate_randomized()

# g.play_sequence()
# print(g.game_grid)
# g.play_sequence()
# print(g.game_grid)
# g.play_sequence()
# print(g.game_grid)
# g.play_sequence()
# print(g.game_grid)
# g.play_sequence()
# print(g.game_grid)
# g.play_sequence()
# print(g.game_grid)
