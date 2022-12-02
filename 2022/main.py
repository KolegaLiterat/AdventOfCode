from src.dataLoader import DataLoader
from src.calories import Calories
from src.rockPaperScissors import Tournament

def day1():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/data/day1.txt").load_data()
    max_calories = Calories(data).get_package_with_highiest_calories()
    
    print(f'Star one solution : {max_calories}')

    sum_of_first_three_packages = Calories(data).get_sum_of_top_three_packages()

    print(f'Star two solution : {sum_of_first_three_packages}')

def day2():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/data/day2.txt").paper_scissors_data()

    rock_paper_scissors_outcome = Tournament(data).run_tournament()

    print(f'Star one solution: {rock_paper_scissors_outcome}')

    rock_paper_scissors_setup_outcome = Tournament(data).run_setupo_tournament()

    print(f'Star one solution: {rock_paper_scissors_setup_outcome}')

def main():
    day2()

if __name__ == "__main__":
    main()