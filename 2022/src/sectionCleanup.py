import numpy as np
from dataclasses import dataclass
from typing import List

@dataclass
class SectionCleanup():
    def __init__(self, data) -> None:
        self.SectionPairs = data
    
    def find_overlaping_sections(self):
        overlaps: int = 0

        for pair in self.SectionPairs:
            id_ranges = self._get_range_for_pairs(pair[0].split("-"), pair[1].split("-"))

            overlaps = overlaps + self._compare_ranges(id_ranges)

        return overlaps
    
    def _get_range_for_pairs(self, pair_one: List[str], pair_two: List[str]):
        range_one, range_two = range(int(pair_one[0]), int(pair_one[1]) + 1), range(int(pair_two[0]), int(pair_two[1]) + 1)

        return range_one, range_two
    
    def _compare_ranges(self, id_ranges):
        overlaps: int = 0
        first_section = np.array(id_ranges[0])
        second_section = np.array(id_ranges[1])

        is_overlap_one_and_two = np.isin(first_section, second_section).all()
        is_overlap_two_and_one = np.isin(second_section, first_section).all()

        if is_overlap_one_and_two == True or is_overlap_two_and_one == True:
            overlaps = 1
        
        return overlaps