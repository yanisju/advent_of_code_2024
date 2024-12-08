import re
from .day import Day
from enum import Enum

class LevelDirection(Enum):
    INCREASING = 0
    DECREASING = 1

class Day2(Day):
    def _get_level_direction(self, number1: int, number2: int) -> LevelDirection:
        if number1 < number2:
            return LevelDirection.INCREASING
        else:
            return LevelDirection.DECREASING
        
    def _get_numbers(self, line: str) -> list[int]:
        """Get every number from a level."""
        pattern = r'\d+'
        p = re.compile(pattern)
        match = p.findall(line)
        numbers = []
        for number in match:
            numbers.append(int(number))
        return numbers

    def _check_line_safety(self, number1: int, number2: int, level_direction = LevelDirection) -> bool:
        condition1 = self._get_level_direction(number1, number2) == level_direction
        condition2 = abs(number1 - number2) > 0 and abs(number1 - number2) < 4 
        if not(condition1 and condition2):
            return False
        else:
            return True
    
    def get_level_is_safe(self, level: list[int]):
        level_direction = self._get_level_direction(level[0], level[1])
        for i in range(len(level) - 1):
            if not self._check_line_safety(level[i], level[i+1], level_direction):
                return False
        return True


    def solve_part_one(self):
        lines = self.read_lines_from_file()
        answer = 0

        for level in lines:
            numbers = self._get_numbers(level)
            if(self.get_level_is_safe(numbers)):
                answer += 1
        return answer

    def get_level_is_safe_dampener(self, level: list[int]):
        if self.get_level_is_safe(level):
            return True
        else:
            for i in range(len(level)):
                tolerated_level = level[:i] + level[i + 1 :]
                if self.get_level_is_safe(tolerated_level):
                    return True
            return False

    def solve_part_two(self):
        lines = self.read_lines_from_file()
        answer = 0

        for level in lines:
            numbers = self._get_numbers(level)
            if(self.get_level_is_safe_dampener(numbers)):
                answer += 1
        return answer


