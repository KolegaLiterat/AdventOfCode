from src.dataLoader import DataLoader
from src.calories import Calories
from src.rockPaperScissors import Tournament
from src.packages import Packages

def day1():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/data/day1.txt").calories_data()
    max_calories = Calories(data).get_package_with_highiest_calories()
    
    print(f'Star one solution : {max_calories}')

    sum_of_first_three_packages = Calories(data).get_sum_of_top_three_packages()

    print(f'Star two solution : {sum_of_first_three_packages}')

def day2():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/data/day2.txt").paper_scissors_data()

    rock_paper_scissors_outcome = Tournament(data).run_tournament()

    print(f'Star one solution: {rock_paper_scissors_outcome}')

    rock_paper_scissors_setup_outcome = Tournament(data).run_setupo_tournament()

    print(f'Star two solution: {rock_paper_scissors_setup_outcome}')

def day3():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/data/day3.txt").packages_data()

    sum_of_priorities = Packages(data).calculate_sum_of_priorities()

    print(f'Star one solution: {sum_of_priorities} ')

def main():
    day3()

if __name__ == "__main__":
    main()