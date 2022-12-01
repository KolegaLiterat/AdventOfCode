from src.dataLoader import DataLoader
from src.calories import Calories

def test_package():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/test_data/day1.txt").load_data()
    
    elf_with_best_package = Calories(data).get_package_with_highiest_calories()

    assert elf_with_best_package == 24000