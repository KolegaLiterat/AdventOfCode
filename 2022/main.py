from src.dataLoader import DataLoader
from src.calories import Calories

def day1():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/data/day1.txt").load_data()
    max_calories = Calories(data).get_package_with_highiest_calories()
    
    print(f'Star one solution : {max_calories}')

    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/data/day1.txt").load_data()
    sum_of_first_three_packages = Calories(data).get_sum_of_top_three_packages()

    print(f'Star two solution : {sum_of_first_three_packages}')

def main():
    day1()

if __name__ == "__main__":
    main()