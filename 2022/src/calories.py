import numpy as np
from dataclasses import dataclass
from typing import List

@dataclass
class Calories():
    def __init__(self, data) -> None:
        self.Data = data
    
    def get_package_with_highiest_calories(self):
        sum_of_calories_with_elf = np.array(self._calculate_calories(), dtype=np.int32)
        
        return sum_of_calories_with_elf.max()
    
    def get_sum_of_top_three_packages(self):
        sum_of_calories_with_elf = np.array(self._calculate_calories(), dtype=np.int32)
        sorted_array = np.sort(sum_of_calories_with_elf)[::-1]

        return sorted_array[0] + sorted_array[1] + sorted_array[2]
    
    def _calculate_calories(self):
        self.Data.append(0)
        
        calories: List[int] = []
        calories_in_packge: int = 0

        for value in self.Data:
            calories_in_packge = calories_in_packge + value
            
            if value == 0:
                calories.append(calories_in_packge)
                calories_in_packge = 0
        
        return calories