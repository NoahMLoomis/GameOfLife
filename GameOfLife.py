from Grid import Grid
import random
import copy


class GameOfLife:
    def __init__(self, game_grid=[], universe_size=4):
        self.game_grid = game_grid
        self.universe_size = universe_size

    def create_grid(self):
        self.game_grid = Grid(square_size=self.universe_size)

    def populate_randomized(self):
        for cell in self.game_grid.grid:
            if random.random() < 0.4:
                self.game_grid.change_alive_status(cell)

    def play_sequence(self):
        grid_copy = copy.deepcopy(self.game_grid)
        for index in range(len(grid_copy.grid)):
            if grid_copy.get_cell_alive_status(grid_copy.grid[index]) == 1:
                self.check_death_conditions(index, grid_copy)
        self.game_grid = grid_copy

    def check_death_conditions(self, index, grid_copy):
        x_pos = grid_copy.grid[index][0]
        y_pos = grid_copy.grid[index][1]

        left = grid_copy.get_cell(x_pos - 1, y_pos)
        right = grid_copy.get_cell(x_pos + 1, y_pos + 1)
        top = grid_copy.get_cell(x_pos, y_pos + 1)
        bottom = grid_copy.get_cell(x_pos, y_pos - 1)
        left_bot_diag = grid_copy.get_cell(x_pos - 1, y_pos - 1)
        right_bot_diag = grid_copy.get_cell(x_pos + 1, y_pos - 1)
        left_top_diag = grid_copy.get_cell(x_pos, y_pos + 1)
        right_top_diag = grid_copy.get_cell(x_pos + 1, y_pos + 1)

        all_checks = [left, right, top, bottom, left_bot_diag,
                      right_bot_diag, left_top_diag, right_top_diag]

        alive_count = 0
        for cell in all_checks:
            if cell[2] == 1:
                alive_count += 1
        if alive_count > 3:
            grid_copy.kill_cell(grid_copy.grid[index])
        elif alive_count >= 2:
            grid_copy.revive_cell(grid_copy.grid[index])
        else:
            grid_copy.kill_cell(grid_copy.grid[index])

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
