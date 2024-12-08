from abc import ABC, abstractmethod

class Day(ABC):
    def __init__(self):
        self.lines = self.read_lines_from_file()

    def read_lines_from_file(self) -> list[str]:
        day_number = type(self).__name__[3:]
        file_name = f"inputs/day{day_number}.txt"
        try:
            with open(file_name, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't find '{file_name}'.")

    @abstractmethod
    def solve_part_one(self) -> None:
        pass

    @abstractmethod
    def solve_part_two(self) -> None:
        pass
