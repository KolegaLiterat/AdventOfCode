from dataclasses import dataclass
from typing import List

@dataclass
class DataLoader:
    data = []

    def __init__(self, file_path: str) -> None:
        self.FilePath: str = file_path

    def load_strings(self) -> List[str]:
        with open(self.FilePath) as input_file:
            data_file = input_file.readlines()
        
        return data_file

    def calories_data(self) -> List[int]:
        advent_of_code_data: List[str] = []

        data_file = self.load_strings()

        for value in data_file:
            advent_of_code_data.append(self._convert_txt_to_int(value))

        return advent_of_code_data

    def paper_scissors_data(self):
        advent_of_code_data: List[str] = []
        
        data_file = self.load_strings()

        for value in data_file:
            advent_of_code_data.append(self._save_match_data(value))

        return advent_of_code_data
    
    def packages_data(self):
        advent_of_code_data: List[str] = []

        data_file = self.load_strings()

        for value in data_file:
            advent_of_code_data.append(self._separate_packages(value[:-1]))
            
        return advent_of_code_data
    
    def elf_groups_data(self):
        advent_of_code_data: List[str] = []
        group_packages: List[str] = []
        group_id: int = 0

        data_file = self.load_strings()

        for value in data_file:
            group_packages.append(value[:-1])
            group_id = group_id + 1

            if group_id == 3:
                advent_of_code_data.append(group_packages.copy())
                group_packages.clear()
                group_id = 0

        return advent_of_code_data
    
    def _convert_txt_to_int(self, value: str) -> int:
        new_value : int = -1

        if value == '\n':
            new_value = 0
        else:
            new_value = int(value)
        
        return new_value
    
    def _save_match_data(self, value: str) -> List[str]:
        match = value[:3].split(" ")

        return match
    
    def _separate_packages(self, value: str) -> List[str]:
        first_package, second_package = value[:len(value)//2], value[len(value)//2:]

        return first_package, second_package
        