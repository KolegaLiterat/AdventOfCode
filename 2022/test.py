from src.dataLoader import DataLoader
from src.calories import Calories

def test_package():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/test_data/day1.txt").load_data()
    
    elf_with_best_package = Calories(data).get_package_with_highiest_calories()

    assert elf_with_best_package == 24000

def test_sum_of_top_three():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/test_data/day1.txt").load_data()
    
    sum_of_top_three_pacakges = Calories(data).get_sum_of_top_three_packages()

    assert sum_of_top_three_pacakges == 45000