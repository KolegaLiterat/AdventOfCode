from src.dataLoader import DataLoader
from src.calories import Calories

def day1():
    data = DataLoader("/Volumes/OutsideMac/Repozytoria/AdventOfCode/AdventOfCode/2022/data/day1.txt").load_data()
    max_calories = Calories(data).get_package_with_highiest_calories()
    
    print(f'Star one solution : {max_calories}')


def main():
    day1()

if __name__ == "__main__":
    main()