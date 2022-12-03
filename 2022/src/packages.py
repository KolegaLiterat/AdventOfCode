import numpy as np
import string
from dataclasses import dataclass

@dataclass
class Packages():
    def __init__(self, data) -> None:
        self.PackagesData = data
        self.PrioritiesValues = {}

    def _build_priorities_values(self):
        lowercase_value: int = 1
        uppercase_value: int = 27

        for char in string.ascii_lowercase:
            self.PrioritiesValues[char] = lowercase_value
            lowercase_value = lowercase_value + 1
        
        for char in string.ascii_uppercase:
            self.PrioritiesValues[char] = uppercase_value
            uppercase_value = uppercase_value + 1

    def calculate_sum_of_priorities(self):
        self._build_priorities_values()

        priorities_sum: int = 0
        test = 0
        
        for package in self.PackagesData:
            item = self._find_the_same_item(package)
            item_value = self.PrioritiesValues[item[0]]

            if len(item) != 1:
                item_value = self.PrioritiesValues[item[1]]
            
            priorities_sum = priorities_sum + item_value
        
        return priorities_sum
    
    def _find_the_same_item(self, package):
        item = np.intersect1d(list(package[0]), list(package[1]))

        return item