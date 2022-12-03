from src.dataLoader import DataLoader
from src.calories import Calories
from src.rockPaperScissors import Tournament

def test_package():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/test_data/day1.txt").calories_data()
    
    elf_with_best_package = Calories(data).get_package_with_highiest_calories()

    assert elf_with_best_package == 24000

def test_sum_of_top_three():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/test_data/day1.txt").calories_data()
    
    sum_of_top_three_pacakges = Calories(data).get_sum_of_top_three_packages()

    assert sum_of_top_three_pacakges == 45000

def test_rock_paper_scissors_winning():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/test_data/day2.txt").paper_scissors_data()

    rock_paper_scissors_outcome = Tournament(data).run_tournament()

    assert rock_paper_scissors_outcome == 15

def test_rock_paper_scissors_setup_torunament():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/test_data/day2.txt").paper_scissors_data()

    rock_paper_scissors_setup_outcome = Tournament(data).run_setupo_tournament()

    assert rock_paper_scissors_setup_outcome == 12

def test_item_rearrangement():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/test_data/day3.txt").packages_data()

    sum_of_priorities = 0

    assert sum_of_priorities == 157