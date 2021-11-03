class Grid:
    def __init__(self, rows, grid=[]):
        self.rows = rows
        self.grid = grid
        
        if self.grid == []:
            for row in range(rows):
                for col in range(rows):
                    self.grid.append([row, col, 0])
                    
    def __str__(self):
        print(f'{"X":^10}{"Y":^10}{"Priority":^10}',)
        print()
        for cell in self.grid:
            print(f'{cell[0]:^10}{cell[1]:^10}{cell[2]:^10}')
            
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
    
    def kill_cell(self, cell):
        cell[2] = 0
        
    def revive_cell(self, cell):
        cell[2] = 1
        

    def get_cell_alive_status(self, cell):
        return cell[2]