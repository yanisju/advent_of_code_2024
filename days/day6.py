from .day import Day
from utils.matrix_navigator import MatrixNavigator, MatrixDirection

class MatrixNavigatorDay6(MatrixNavigator):
    def advance_position(self):
        if self.direction == MatrixDirection.UP and self.get_char_up() == ['#']:
            self.direction = MatrixDirection.RIGHT
            return self.advance_position()
        elif self.direction == MatrixDirection.RIGHT and self.get_char_right() == ['#']:
            self.direction = MatrixDirection.DOWN
            return self.advance_position()
        elif self.direction == MatrixDirection.DOWN and self.get_char_down() == ['#']:
            self.direction = MatrixDirection.LEFT
            return self.advance_position()
        elif self.direction == MatrixDirection.LEFT and self.get_char_left() == ['#']:
            self.direction = MatrixDirection.UP
            return self.advance_position()
        else:
            return super().advance_position()

class Day6(Day):
    def solve_part_one(self):
        matrix_navigator = MatrixNavigatorDay6(self.lines)
        guard_initial_position = matrix_navigator.find_char_position('^')
        matrix_navigator.set_position(guard_initial_position[0], guard_initial_position[1])

        positions = set()
        is_guard_out = False
        while not is_guard_out:
            positions.add((matrix_navigator.x_pos, matrix_navigator.y_pos))
            if not matrix_navigator.advance_position():
                is_guard_out = True
        return len(positions)
    
    def check_if_obstruction_lead_to_loop(self, matrix, y, x, guard_initial_position):
        line_to_obstrucate = matrix[y][:x] + '#' + matrix[y][x + 1:]
        new_lines = list(matrix)
        new_lines[y] = line_to_obstrucate
        matrix_navigator_obstruction = MatrixNavigatorDay6(new_lines)
        matrix_navigator_obstruction.set_position(guard_initial_position[0], guard_initial_position[1])
        is_guard_out = False
        guard_back_to_initial_pos = False

        visited = set()
        while not is_guard_out and not guard_back_to_initial_pos:
            combo = (((matrix_navigator_obstruction.x_pos, matrix_navigator_obstruction.y_pos)), matrix_navigator_obstruction.direction)
            if combo in visited:
                guard_back_to_initial_pos = True
            visited.add(combo)
            if not matrix_navigator_obstruction.advance_position():
                is_guard_out = True
            
        if guard_back_to_initial_pos:
            return True
        else:
            False  
    
    def solve_part_two(self):
        matrix_navigator = MatrixNavigatorDay6(self.lines)
        guard_initial_position = matrix_navigator.find_char_position('^')
        answer = 0

        for i in range((matrix_navigator.y_length * matrix_navigator.x_length) - 1):
            if matrix_navigator.get_current_char() == '.':
                if self.check_if_obstruction_lead_to_loop(matrix_navigator.matrix, matrix_navigator.y_pos, matrix_navigator.x_pos, guard_initial_position):
                    answer += 1
            matrix_navigator.advance()
        return answer