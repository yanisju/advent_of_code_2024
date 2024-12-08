import re
from .day import Day

class Day1(Day):
    def _get_numbers(self):
        left_numbers = []
        right_numbers = []
        pattern = r'\d+'
        p = re.compile(pattern)

        lines = self.read_lines_from_file()
        for line in lines:
            match = p.findall(line)
            left_numbers.append(int(match[0]))
            right_numbers.append(int(match[1]))
        left_numbers.sort()
        right_numbers.sort()
        return left_numbers, right_numbers

    def solve_part_one(self):
        left_numbers, right_numbers = self._get_numbers()
        answer = 0
        for i in range(len(left_numbers)):
            answer += abs(left_numbers[i] - right_numbers[i])
        return answer
    
    def solve_part_two(self):
        left_numbers, right_numbers = self._get_numbers()
        answer = 0
        for number in left_numbers:
            answer += number * right_numbers.count(number)
        return answer