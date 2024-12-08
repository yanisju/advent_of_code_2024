from .day import Day
from utils.matrix_navigator import MatrixNavigator

class Day4(Day):
    def check_if_xmas_string(self, matrix_navigator: MatrixNavigator) -> bool:
        xmas_found_count = 0
        mas_list = ['M', 'A', 'S']
        up = (matrix_navigator.get_char_up(3) == mas_list)
        if up:
            xmas_found_count += 1
        down = (matrix_navigator.get_char_down(3) == mas_list)
        if down:
            xmas_found_count += 1
        left = (matrix_navigator.get_char_left(3) == mas_list)
        if left:
            xmas_found_count += 1
        right = (matrix_navigator.get_char_right(3) == mas_list)
        if right:
            xmas_found_count += 1
        up_left = (matrix_navigator.get_char_up_left(3) == mas_list)
        if up_left:
            xmas_found_count += 1
        up_right = (matrix_navigator.get_char_up_right(3) == mas_list)
        if up_right:
            xmas_found_count += 1
        down_left = (matrix_navigator.get_char_down_left(3) == mas_list)
        if down_left:
            xmas_found_count += 1
        down_right = (matrix_navigator.get_char_down_right(3) == mas_list)
        if down_right:
            xmas_found_count += 1
        return xmas_found_count

    def solve_part_one(self):
        answer = 0
        matrix_navigator = MatrixNavigator(self.lines)
        for i in range(matrix_navigator.x_length * matrix_navigator.y_length):
            if matrix_navigator.get_current_char() == "X":
                answer += self.check_if_xmas_string(matrix_navigator)
            matrix_navigator.advance()
        return answer
    
    def check_if_xmas_string_part_two(self, matrix_navigator: MatrixNavigator) -> bool:
        m = ['M']
        s = ['S']
        
        up_left_char = matrix_navigator.get_char_up_left()
        up_right_char = matrix_navigator.get_char_up_right()
        down_left_char = matrix_navigator.get_char_down_left()
        down_right_char = matrix_navigator.get_char_down_right()
        config1 = (up_left_char == m and up_right_char == m and down_left_char == s and down_right_char == s) 
        config2 = (up_left_char == m and up_right_char == s and down_left_char == m and down_right_char == s) 
        config3 = (up_left_char == s and up_right_char == s and down_left_char == m and down_right_char == m) 
        config4 = (up_left_char == s and up_right_char == m and down_left_char == s and down_right_char == m) 
        if config1 or config2 or config3 or config4:
            return True
        else:
            return False
    
    def solve_part_two(self):
        answer = 0
        matrix_navigator = MatrixNavigator(self.lines)
        for i in range(matrix_navigator.x_length * matrix_navigator.y_length):
            if matrix_navigator.get_current_char() == 'A':
                if self.check_if_xmas_string_part_two(matrix_navigator):
                    answer += 1
            matrix_navigator.advance()
        return answer