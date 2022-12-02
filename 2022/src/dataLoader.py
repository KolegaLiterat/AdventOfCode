from dataclasses import dataclass
from typing import List

@dataclass
class DataLoader:
    data = []

    def __init__(self, file_path: str) -> None:
        self.FilePath: str = file_path

    def load_data(self) -> List[int]:
        advent_of_code_data: List[str] = []

        with open(self.FilePath) as data_file:
            data: List[str] = data_file.readlines()

        for value in data:
            advent_of_code_data.append(self._convert_txt_to_int(value))

        return advent_of_code_data

    def paper_scissors_data(self):
        advent_of_code_data: List[str] = []
        
        with open(self.FilePath) as data_file:
            data: List[str] = data_file.readlines()

        for value in data:
            advent_of_code_data.append(self._save_match_data(value))

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
        