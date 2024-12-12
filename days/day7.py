from .day import Day
from itertools import product

class Day7(Day):
    def get_numbers(self):
        targets = []
        numbers = []
        for line in self.lines:
            target, num_whitespace = line.split(':')
            num = list(map(int, num_whitespace.split()))
            targets.append(int(target))
            numbers.append(num)
        return targets, numbers
    
    def is_equation_true(self, target: int, numbers: list[int]):
        possible_combinaison = product('+*', repeat=len(numbers) - 1)
        calibration_result = 0

        for combinaison in possible_combinaison:
            i = 0
            calibration_result = 0
            for operator in combinaison:
                
                if operator == '+' and i == 0:
                    calibration_result = numbers[0] + numbers[1]
                elif operator == '+' and i != 0:
                    calibration_result +=  numbers[i + 1]
                elif operator == '*' and i == 0:
                    calibration_result = numbers[0] * numbers[1]
                else:
                    calibration_result *= numbers[i + 1]
                i += 1
            if calibration_result == target:
                return True
        return False

    def solve_part_one(self):
        answer = 0
        targets, numbers = self.get_numbers()
        for i in range(len(targets)):
            if self.is_equation_true(targets[i], numbers[i]):
                answer += targets[i]
        return answer
    
    def is_equation_true_part_two(self, target: int, numbers: list[int]):
        possible_combinaison = product('+*|', repeat=len(numbers) - 1)
        calibration_result = 0

        for combinaison in possible_combinaison:
            i = 0
            calibration_result = 0
            for operator in combinaison:
                if operator == '+' and i == 0:
                    calibration_result = numbers[0] + numbers[1]
                elif operator == '+' and i != 0:
                    calibration_result +=  numbers[i + 1]
                elif operator == '|' and i == 0:
                    calibration_result = int(str(numbers[0]) + str(numbers[1]))
                elif operator == '|' and i != 0:
                    calibration_result = int(str(calibration_result) + str(numbers[i + 1]))
                elif operator == '*' and i == 0:
                    calibration_result = numbers[0] * numbers[1]
                else:
                    calibration_result *= numbers[i + 1]
                i += 1
            if calibration_result == target:
                return True
        return False
    
    def solve_part_two(self):
        answer = 0
        targets, numbers = self.get_numbers()
        for i in range(len(targets)):
            if self.is_equation_true_part_two(targets[i], numbers[i]):
                answer += targets[i]
        return answer