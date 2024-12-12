from enum import Enum

class MatrixDirection(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class MatrixNavigator:
    """Help to navigate through a 2D-array. """
    def __init__(self, matrix: list[list]):
        self.matrix = matrix
        self.y_length = len(matrix)
        self.x_length = len(matrix[0])
        self.x_pos = 0
        self.y_pos = 0
        self.direction = MatrixDirection.UP

    def set_position(self, x: int, y: int) -> bool:
        if x > 0 and x < self.x_length and y > 0 and y < self.y_length:
            self.x_pos = x
            self.y_pos = y
            return True
        else:
            return False
        
    def set_direction(self, direction: MatrixDirection):
        self.direction = direction

    def set_char_at_index(self, y, x, char):
        new_line = self.matrix[y][:x] + char + self.matrix[y][x + 1:]
        self.matrix[y] = new_line

    def advance(self):
        if self.x_pos == self.x_length - 1:
            self.x_pos = 0
            if self.y_pos == self.y_length - 1: # Come back to beginning
                self.y_pos = 0
            else:
                self.y_pos += 1
        else:
            self.x_pos += 1

    def advance_position(self) -> bool:
        if self.direction == MatrixDirection.UP:
            return self.move_up()
        elif self.direction == MatrixDirection.DOWN:
            return self.move_down()
        elif self.direction == MatrixDirection.RIGHT:
            return self.move_right()
        elif self.direction == MatrixDirection.LEFT:
            return self.move_left()
        
    def get_char_right(self, n=1):
        if self.x_pos + n < self.x_length:
            return [self.matrix[self.y_pos][self.x_pos + i] for i in range(1, n + 1)]
        return None

    def get_char_left(self, n=1):
        if self.x_pos - n >= 0:
            return [self.matrix[self.y_pos][self.x_pos - i] for i in range(1, n + 1)]
        return None

    def get_char_up(self, n=1):
        if self.y_pos - n >= 0:
            return [self.matrix[self.y_pos - i][self.x_pos] for i in range(1, n + 1)]
        return None

    def get_char_down(self, n=1):
        if self.y_pos + n < self.y_length:
            return [self.matrix[self.y_pos + i][self.x_pos] for i in range(1, n + 1)]
        return None

    def get_char_up_right(self, n=1):
        if self.y_pos - n >= 0 and self.x_pos + n < self.x_length:
            return [self.matrix[self.y_pos - i][self.x_pos + i] for i in range(1, n + 1)]
        return None

    def get_char_up_left(self, n=1):
        if self.y_pos - n >= 0 and self.x_pos - n >= 0:
            return [self.matrix[self.y_pos - i][self.x_pos - i] for i in range(1, n + 1)]
        return None

    def get_char_down_right(self, n=1):
        if self.y_pos + n < self.y_length and self.x_pos + n < self.x_length:
            return [self.matrix[self.y_pos + i][self.x_pos + i] for i in range(1, n + 1)]
        return None

    def get_char_down_left(self, n=1):
        if self.y_pos + n < self.y_length and self.x_pos - n >= 0:
            return [self.matrix[self.y_pos + i][self.x_pos - i] for i in range(1, n + 1)]
        return None

    def move_right(self) -> bool:
        if self.x_pos + 1 < self.x_length:
            self.x_pos += 1
            return True
        else:  
            return False

    def move_left(self) -> bool:
        if self.x_pos - 1 >= 0:
            self.x_pos -= 1
            return True
        else:  
            return False

    def move_up(self) -> bool:
        if self.y_pos - 1 >= 0:
            self.y_pos -= 1
            return True
        else:  
            return False

    def move_down(self) -> bool:
        if self.y_pos + 1 < self.y_length:
            self.y_pos += 1
            return True
        else:  
            return False

    def move_up_right(self) -> bool:
        if self.y_pos - 1 >= 0 and self.x_pos + 1 < self.x_length:
            self.y_pos -= 1
            self.x_pos += 1
            return True
        else:  
            return False

    def move_up_left(self) -> bool:
        if self.y_pos - 1 >= 0 and self.x_pos - 1 >= 0:
            self.y_pos -= 1
            self.x_pos -= 1
            return True
        else:  
            return False

    def move_down_right(self) -> bool:
        if self.y_pos + 1 < self.y_length and self.x_pos + 1 < self.x_length:
            self.y_pos += 1
            self.x_pos += 1
            return True
        else:  
            return False

    def move_down_left(self) -> bool:
        if self.y_pos + 1 < self.y_length and self.x_pos - 1 >= 0:
            self.y_pos += 1
            self.x_pos -= 1
            return True
        else:  
            return False

    def get_current_char(self):
        return self.matrix[self.y_pos][self.x_pos]

    def find_char_position(self, char):
        for row_idx, row in enumerate(self.matrix):
            if char in row:
                col_idx = row.index(char)
                return col_idx, row_idx
        return None