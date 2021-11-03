import os

class InvalidFileFormatException(BaseException):
    pass

class FileReading():
    def __init__(self, file_name):
        file_path = f'lifeFiles/{file_name}'
        
        if not os.path.isfile(f'lifeFiles/{file_name}'):
            raise FileNotFoundError(f'The file with the name {file_name} does not exist')
        self.file_path = file_path
        
        self.grid = self.parse_file_to_grid()
        
        self.rows = self.check_rows_cols_count()
        self.check_file_format()
        
    def check_rows_cols_count(self):
        rows = len(open(self.file_path).readlines())
        cols = len(open(self.file_path).readline().strip("\n"))
        if rows != cols:
            raise InvalidFileFormatException("The number of rows and columns must be the same")
        return rows
        
    def check_file_format(self):
        for line in open(self.file_path).readlines():
            for cell in line.strip("\n"):
                if cell != '1' and cell != '0':
                    raise InvalidFileFormatException("The file can only contain 1's or 0's")
                
    def transform_to_grid(self):
        new_grid = []
        total_count = 0
        for row in range(self.rows):
            for col in range(self.rows):
                new_grid.append([row, col, self.grid[total_count]])
                total_count += 1
        return new_grid
    
    def parse_file_to_grid(self):
        parsed_cells = []
        for line in open(self.file_path).readlines():
            for cell in line:
                if cell != "\n":
                    parsed_cells.append(int(cell))
        return parsed_cells