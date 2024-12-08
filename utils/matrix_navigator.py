class MatrixNavigator:
    """Help to navigate through a 2D-array. """
    def __init__(self, matrix: list[list]):
        self.matrix = matrix
        self.y_length = len(matrix)
        self.x_length = len(matrix[0])
        self.x_pos = 0
        self.y_pos = 0

    def advance(self):
        if self.x_pos == self.x_length - 1:
            self.x_pos = 0
            if self.y_pos == self.y_length - 1: # Come back to beginning
                self.y_pos = 0
            else:
                self.y_pos += 1
        else:
            self.x_pos += 1
        
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

    def move_right(self):
        if self.x_pos + 1 < self.x_length:
            self.x_pos += 1

    def move_left(self):
        if self.x_pos - 1 >= 0:
            self.x_pos -= 1

    def move_up(self):
        if self.y_pos - 1 >= 0:
            self.y_pos -= 1

    def move_down(self):
        if self.y_pos + 1 < self.y_length:
            self.y_pos += 1

    def move_up_right(self):
        if self.y_pos - 1 >= 0 and self.x_pos + 1 < self.x_length:
            self.y_pos -= 1
            self.x_pos += 1

    def move_up_left(self):
        if self.y_pos - 1 >= 0 and self.x_pos - 1 >= 0:
            self.y_pos -= 1
            self.x_pos -= 1

    def move_down_right(self):
        if self.y_pos + 1 < self.y_length and self.x_pos + 1 < self.x_length:
            self.y_pos += 1
            self.x_pos += 1

    def move_down_left(self):
        if self.y_pos + 1 < self.y_length and self.x_pos - 1 >= 0:
            self.y_pos += 1
            self.x_pos -= 1

    def get_current_char(self):
        return self.matrix[self.y_pos][self.x_pos]
