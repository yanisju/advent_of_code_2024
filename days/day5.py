import re
from itertools import permutations
from .day import Day

class Day5(Day):
    def get_data(self):
        first_section =[]
        second_section = []
        pattern = r'\d+'
        p1 = re.compile(pattern)
        for line in self.lines:
            match = re.findall(p1, line)
            if '|' in line:
                    first_section.append((int(match[0]), int(match[1])))
            else:
                numbers = []
                for number in match:
                    numbers.append(int(number))
                if numbers != []:
                    second_section.append(numbers)
        return first_section, second_section

    def is_line_valid(self, page_rules: list[int], line: list[int]) -> bool:
        for page_rule in page_rules:
            page_one = page_rule[0]
            page_two = page_rule[1]
            if page_one in line and page_two in line and line.index(page_one) > line.index(page_two):
                    return False
        return True
        
    def get_middle_page_number(self, line: list[int]):
        index = int(len(line) / 2)
        return line[index]

    def solve_part_one(self):
        answer = 0
        first_section, second_section = self.get_data()
        for line in second_section:
            line_is_valid = self.is_line_valid(first_section, line)
            if line_is_valid:
                answer += self.get_middle_page_number(line)
        return answer
    
    def get_line_correct(self, page_rules: list[int], line: list[int]):
        for line_permuted in permutations(line):
            if self.is_line_valid(page_rules, line_permuted):
                return line_permuted
    
    def solve_part_two(self):
        answer = 0
        i = 0
        first_section, second_section = self.get_data()
        for line in second_section:
            line_is_valid = self.is_line_valid(first_section, line)
            if line_is_valid:
                answer += self.get_middle_page_number(line)
            else:
                line_correct = self.get_line_correct(first_section, line)
                answer += self.get_middle_page_number(line_correct)
            i += 1
            print(i)
        return answer