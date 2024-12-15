from .day import Day
from utils.matrix_navigator import MatrixNavigator

class Day8(Day):
    def get_antinode1_pos(self, antenna1_pos, antenna2_pos, range = 1):
        y1, x1 = antenna1_pos
        y2, x2 = antenna2_pos
        if x1 >= x2:
            antinode1_x = x1 + abs(x1 - x2) * range
        else:
            antinode1_x = x1 - abs(x1 - x2) * range
        antinode1_y = y1 - abs(y1 - y2) * range
        return (antinode1_y, antinode1_x)

    def get_antinode2_pos(self, antenna1_pos, antenna2_pos, range = 1):
        y1, x1 = antenna1_pos
        y2, x2 = antenna2_pos
        if x1 >= x2:
            antinode2_x = x2 - abs(x1 - x2) * range
        else:
            antinode2_x = x2 + abs(x1 - x2) * range
        antinode2_y = y2 + abs(y1 - y2) * range
        return (antinode2_y, antinode2_x)
    
    def get_antinodes_position(self, antenna1_pos, antenna2_pos):
        """Y2 is always =< to Y1. """
        y1, x1 = antenna1_pos
        y2, x2 = antenna2_pos
        if x1 >= x2:
            antinode1_x = x1 + abs(x1 - x2)
            antinode2_x = x2 - abs(x1 - x2)
        else:
            antinode1_x = x1 - abs(x1 - x2)
            antinode2_x = x2 + abs(x1 - x2)
        antinode1_y = y1 - abs(y1 - y2)
        antinode2_y = y2 + abs(y1 - y2)
        return (antinode1_y, antinode1_x), (antinode2_y, antinode2_x)
    
    def add_antinodes_if_valid(self, antenna1_pos, antenna2_pos, valid_antidones_pos: set, matrix_navigator: MatrixNavigator):
        antinode1_pos = self.get_antinode1_pos(antenna1_pos, antenna2_pos)
        antinode2_pos = self.get_antinode2_pos(antenna1_pos, antenna2_pos)
        y_length = matrix_navigator.y_length
        x_length = matrix_navigator.x_length
        if antinode1_pos[0] >= 0 and antinode1_pos[0] < y_length and antinode1_pos[1] >= 0 and antinode1_pos[1] < x_length:
            valid_antidones_pos.add(antinode1_pos)
        if antinode2_pos[0] >= 0 and antinode2_pos[0] < y_length and antinode2_pos[1] >= 0 and antinode2_pos[1] < x_length:
            valid_antidones_pos.add(antinode2_pos)

    def solve_part_one(self):
        matrix_navigator = MatrixNavigator(self.lines)
        frequency_count = {}
        valid_antidones_pos = set()
        for i in range((matrix_navigator.x_length * matrix_navigator.y_length)):
            current_char = matrix_navigator.get_current_char()
            char_pos = (matrix_navigator.y_pos, matrix_navigator.x_pos)
            if current_char != ".":
                if current_char not in frequency_count:
                    frequency_count[current_char] = [1, []]
                else:
                    frequency_count[current_char][0] += 1
                    for antennas_pos in frequency_count[current_char][1]:
                        self.add_antinodes_if_valid(antennas_pos, char_pos, valid_antidones_pos, matrix_navigator)
                frequency_count[current_char][1].append(char_pos)
            matrix_navigator.advance()
        return len(valid_antidones_pos)
    
    def add_antinodes_if_valid_part_two(self, antenna1_pos, antenna2_pos, valid_antidones_pos: set, matrix_navigator: MatrixNavigator):
        antinode1_pos = self.get_antinode1_pos(antenna1_pos, antenna2_pos)
        antinode2_pos = self.get_antinode2_pos(antenna1_pos, antenna2_pos)
        y_length = matrix_navigator.y_length
        x_length = matrix_navigator.x_length

        i = 1
        condition_antinode1 = antinode1_pos[0] >= 0 and antinode1_pos[0] < y_length and antinode1_pos[1] >= 0 and antinode1_pos[1] < x_length
        while(condition_antinode1):
            valid_antidones_pos.add(antinode1_pos)
            i += 1
            antinode1_pos = self.get_antinode1_pos(antenna1_pos, antenna2_pos, i)
            condition_antinode1 = antinode1_pos[0] >= 0 and antinode1_pos[0] < y_length and antinode1_pos[1] >= 0 and antinode1_pos[1] < x_length

        i = 1
        condition_antinode2 = antinode2_pos[0] >= 0 and antinode2_pos[0] < y_length and antinode2_pos[1] >= 0 and antinode2_pos[1] < x_length
        while(condition_antinode2):
            valid_antidones_pos.add(antinode2_pos)
            i += 1
            antinode2_pos = self.get_antinode2_pos(antenna1_pos, antenna2_pos, i)
            condition_antinode2 = antinode2_pos[0] >= 0 and antinode2_pos[0] < y_length and antinode2_pos[1] >= 0 and antinode2_pos[1] < x_length

    def solve_part_two(self):
        matrix_navigator = MatrixNavigator(self.lines)
        frequency_count = {}
        valid_antidones_pos = set()
        for i in range((matrix_navigator.x_length * matrix_navigator.y_length)):
            current_char = matrix_navigator.get_current_char()
            char_pos = (matrix_navigator.y_pos, matrix_navigator.x_pos)
            if current_char != ".":
                valid_antidones_pos.add(char_pos) # Add antenna
                if current_char not in frequency_count:
                    frequency_count[current_char] = [1, []]
                else:
                    frequency_count[current_char][0] += 1
                    for antennas_pos in frequency_count[current_char][1]:
                        self.add_antinodes_if_valid_part_two(antennas_pos, char_pos, valid_antidones_pos, matrix_navigator)
                frequency_count[current_char][1].append(char_pos)
            matrix_navigator.advance()
        return len(valid_antidones_pos)