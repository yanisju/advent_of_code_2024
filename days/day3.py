import re
from .day import Day

class Day3(Day):
    def _multiply_mul_instruction(self, mul_instruction: str):
        pattern = r'\d+'
        p = re.compile(pattern)
        match = p.findall(mul_instruction)
        return int(match[0]) * int(match[1]) 


    def _get_mul_instruction(self):
        instructions = []
        pattern = r'(mul\(\d{1,3},\d{1,3}\))'
        p = re.compile(pattern)
        for line in self.read_lines_from_file():
            match = p.findall(line)
            instructions.extend(match)
        return instructions

    def solve_part_one(self):
        answer = 0
        instructions = self._get_mul_instruction()
        for one_instruction in instructions:
            print(one_instruction)
            answer += self._multiply_mul_instruction(one_instruction)
        return answer


    def get_instructions_pos(self) -> list[int]:
        char_read_count = 0
        instructions = {}
        pattern = re.compile(r'(do\(\)|don\'t\(\))')
        for line in self.read_lines_from_file():
            matches = re.finditer(pattern, line)
            for match in matches:
                position = int(match.start()) + char_read_count
                if match.group() == 'do()':
                    instructions[position] = "do()"
                else:
                    instructions[position] = "don't()"
            char_read_count += len(line)
        return instructions
    
    def get_do_instructions_validity(self, instructions: dict):
        is_valid = True
        start_pos = 0
        validity_range = []
        for pos in instructions.keys():
            if is_valid and instructions[pos] == "don't()":
                validity_range.append((start_pos, pos))
                is_valid = False
            elif not is_valid and instructions[pos] == "do()":
                is_valid = True
                start_pos = pos
        return validity_range
    
    def _get_mul_instruction_and_pos(self):
        instructions_and_pos = []
        char_read_count = 0
        pattern = r'(mul\(\d{1,3},\d{1,3}\))'
        p = re.compile(pattern)
        for line in self.read_lines_from_file():
            matches = p.finditer(line)
            for match in matches:
                position = int(match.start()) + char_read_count
                instructions_and_pos.append((match.group(), position))
            char_read_count += len(line)
        return instructions_and_pos
        
    def solve_part_two(self):
        answer = 0
        instructions = self.get_instructions_pos()
        instructions_validity_range = self.get_do_instructions_validity(instructions)
        mul_instructions_and_pos_array = self._get_mul_instruction_and_pos()
        for mul_instructions_and_pos in mul_instructions_and_pos_array:
            pos = mul_instructions_and_pos[1]
            for validity_range in instructions_validity_range:
                if pos > validity_range[0] and pos < validity_range[1]:
                    answer += self._multiply_mul_instruction(mul_instructions_and_pos[0])
        return answer